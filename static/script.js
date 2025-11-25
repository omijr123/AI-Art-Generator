class ArtGenerator {
    constructor() {
        this.currentResultUrl = '';
        this.currentResultType = '';
        this.isDarkMode = false;
        this.initializeApp();
    }

    initializeApp() {
        this.initializeTheme();
        this.initializeEventListeners();
        this.checkServerHealth();
    }

    initializeTheme() {
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        this.isDarkMode = savedTheme === 'dark' || (!savedTheme && prefersDark);
        this.applyTheme();

        document.getElementById('theme-toggle').addEventListener('click', () => {
            this.toggleTheme();
        });
    }

    toggleTheme() {
        this.isDarkMode = !this.isDarkMode;
        this.applyTheme();
        localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light');
    }

    applyTheme() {
        const theme = this.isDarkMode ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        
        const themeIcon = document.querySelector('.theme-icon');
        themeIcon.textContent = this.isDarkMode ? '☀️' : '🌙';
    }

    initializeEventListeners() {
        const promptTextarea = document.getElementById('prompt');
        const charCount = document.getElementById('char-count');
        
        promptTextarea.addEventListener('input', (e) => {
            const length = e.target.value.length;
            charCount.textContent = `${length}/500`;
            
            if (length > 450) {
                charCount.style.color = 'var(--error-color)';
            } else if (length > 400) {
                charCount.style.color = 'var(--warning-color)';
            } else {
                charCount.style.color = 'var(--text-muted)';
            }
        });

        document.getElementById('generateImage').addEventListener('click', () => {
            this.generateArt('image');
        });

        document.getElementById('generateVideo').addEventListener('click', () => {
            this.generateArt('video');
        });

        document.getElementById('close-result').addEventListener('click', () => {
            this.hideResult();
        });

        document.getElementById('downloadBtn').addEventListener('click', () => {
            this.downloadResult();
        });

        document.getElementById('generateAgain').addEventListener('click', () => {
            this.hideResult();
            document.getElementById('prompt').focus();
        });

        document.getElementById('retryBtn').addEventListener('click', () => {
            this.hideError();
            this.generateArt(this.currentResultType);
        });

        promptTextarea.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                this.generateArt('image');
            }
        });
    }

    async generateArt(type) {
        const prompt = document.getElementById('prompt').value.trim();
        const style = document.getElementById('style').value;
        const duration = document.getElementById('duration').value;
        const enhancePrompt = document.getElementById('enhancePrompt').checked;

        if (!prompt) {
            this.showError('Please describe your vision to generate art');
            return;
        }

        if (prompt.length < 5) {
            this.showError('Please provide a more detailed description (at least 5 characters)');
            return;
        }

        this.showLoading();
        this.hideResult();
        this.hideError();

        try {
            const endpoint = type === 'image' ? '/generate/image' : '/generate/video';
            const payload = {
                prompt: prompt,
                style: style,
                enhance_prompt: enhancePrompt
            };

            if (type === 'video') {
                payload.duration = parseInt(duration);
            }

            console.log(`🚀 Generating ${type} with:`, payload);

            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload)
            });

            const result = await response.json();
            console.log(`📦 ${type} generation result:`, result);

            if (result.success) {
                this.currentResultUrl = type === 'image' ? result.image_url : result.video_url;
                this.currentResultType = type;
                console.log(`✅ ${type} URL:`, this.currentResultUrl);
                this.showResult(result);
            } else {
                throw new Error(result.error || 'Generation failed');
            }

        } catch (error) {
            console.error('❌ Generation error:', error);
            this.showError(error.message);
        } finally {
            this.hideLoading();
        }
    }

    showLoading() {
        document.getElementById('loading').classList.remove('hidden');
        document.getElementById('generateImage').disabled = true;
        document.getElementById('generateVideo').disabled = true;
    }

    hideLoading() {
        document.getElementById('loading').classList.add('hidden');
        document.getElementById('generateImage').disabled = false;
        document.getElementById('generateVideo').disabled = false;
    }

    showResult(data) {
        const resultCard = document.getElementById('result');
        const outputImage = document.getElementById('outputImage');
        const outputVideo = document.getElementById('outputVideo');
        const resultInfo = document.getElementById('resultInfo');
        const downloadBtn = document.getElementById('downloadBtn');

        // Hide both media elements first
        outputImage.classList.add('hidden');
        outputVideo.classList.add('hidden');

        // Clear any previous video sources
        outputVideo.innerHTML = 'Your browser does not support the video tag.';

        if (this.currentResultType === 'image') {
            // For images
            const imageUrl = this.currentResultUrl + '?t=' + new Date().getTime();
            console.log('🖼️ Loading image:', imageUrl);
            
            outputImage.src = imageUrl;
            outputImage.classList.remove('hidden');
            
            outputImage.onload = () => {
                console.log('✅ Image loaded successfully');
                resultCard.classList.remove('hidden');
                resultCard.classList.add('fade-in');
            };
            
            outputImage.onerror = () => {
                console.error('❌ Failed to load image');
                this.showError('Failed to load generated image. Please try again.');
            };
        } else {
            // For videos
            const videoUrl = this.currentResultUrl + '?t=' + new Date().getTime();
            console.log('🎬 Loading video:', videoUrl);
            
            // Create source element
            const source = document.createElement('source');
            source.src = videoUrl;
            source.type = 'video/mp4';
            
            // Clear and set up video element
            outputVideo.innerHTML = '';
            outputVideo.appendChild(source);
            outputVideo.classList.remove('hidden');
            
            // Add event listeners for video
            outputVideo.onloadeddata = () => {
                console.log('✅ Video loaded successfully');
                resultCard.classList.remove('hidden');
                resultCard.classList.add('fade-in');
                
                // Try to play the video
                outputVideo.play().catch(e => {
                    console.log('⚠️ Autoplay prevented, user can click play');
                });
            };
            
            outputVideo.onerror = (e) => {
                console.error('❌ Video loading error:', e);
                console.error('Video error details:', outputVideo.error);
                this.showError('Failed to load generated video. The video file may be corrupted or the format is not supported.');
            };
            
            outputVideo.onstalled = () => {
                console.log('⚠️ Video playback stalled');
            };
            
            outputVideo.onwaiting = () => {
                console.log('⏳ Video waiting for data');
            };
            
            // Force load the video
            outputVideo.load();
        }

        // Update result info
        let infoHTML = `<strong>Prompt:</strong> ${data.prompt_used || document.getElementById('prompt').value}<br>`;
        infoHTML += `<strong>Generation Time:</strong> ${data.generation_time}s<br>`;
        infoHTML += `<strong>Model:</strong> ${data.model || 'runwayml/stable-diffusion-v1-5'}`;
        
        if (data.note) {
            infoHTML += `<br><em>${data.note}</em>`;
        }
        
        resultInfo.innerHTML = infoHTML;
        downloadBtn.classList.remove('hidden');

        // Scroll to result after a short delay to ensure content is loaded
        setTimeout(() => {
            resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 300);
    }

    showError(message) {
        const errorCard = document.getElementById('error');
        const errorMessage = document.getElementById('errorMessage');
        
        errorMessage.textContent = message;
        errorCard.classList.remove('hidden');
        errorCard.classList.add('fade-in');

        errorCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    hideError() {
        document.getElementById('error').classList.add('hidden');
    }

    hideResult() {
        document.getElementById('result').classList.add('hidden');
        // Reset media elements
        document.getElementById('outputImage').src = '';
        document.getElementById('outputVideo').innerHTML = 'Your browser does not support the video tag.';
    }

    downloadResult() {
        if (this.currentResultUrl) {
            const link = document.createElement('a');
            link.href = this.currentResultUrl;
            link.download = `ai-art-${Date.now()}.${this.currentResultType === 'image' ? 'png' : 'mp4'}`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    }

    async checkServerHealth() {
        try {
            const response = await fetch('/health');
            const data = await response.json();
            console.log('🏥 Server health:', data);
        } catch (error) {
            console.warn('⚠️ Health check failed:', error);
        }
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ArtGenerator();
});