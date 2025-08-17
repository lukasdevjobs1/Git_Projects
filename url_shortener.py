"""
🔗 URL Shortener
Simple and efficient URL shortener using TinyURL API
"""

import streamlit as st
import requests
import re
from urllib.parse import urlparse
import pyperclip

class URLShortener:
    """URL shortener using TinyURL API"""
    
    API_URL = "http://tinyurl.com/api-create.php"
    
    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Validate URL format"""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    @classmethod
    def shorten_url(cls, long_url: str) -> str:
        """Shorten URL using TinyURL API"""
        if not cls.is_valid_url(long_url):
            raise ValueError("Invalid URL format")
        
        try:
            response = requests.get(cls.API_URL, params={'url': long_url}, timeout=10)
            response.raise_for_status()
            
            short_url = response.text.strip()
            if short_url.startswith('http'):
                return short_url
            else:
                raise ValueError("Failed to shorten URL")
                
        except requests.RequestException as e:
            raise ConnectionError(f"API request failed: {str(e)}")

def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="🔗 URL Shortener",
        page_icon="🔗",
        layout="centered"
    )
    
    st.title("🔗 URL Shortener")
    st.markdown("*Simple and fast URL shortening service*")
    
    # Input section
    with st.container():
        url_input = st.text_input(
            "Enter URL to shorten:",
            placeholder="https://example.com/very-long-url",
            help="Enter a valid URL starting with http:// or https://"
        )
        
        col1, col2 = st.columns([1, 3])
        with col1:
            shorten_btn = st.button("🔗 Shorten", type="primary")
    
    # Processing
    if shorten_btn and url_input:
        with st.spinner("Shortening URL..."):
            try:
                short_url = URLShortener.shorten_url(url_input)
                
                # Success display
                st.success("✅ URL shortened successfully!")
                
                # Results section
                with st.container():
                    st.markdown("### Results")
                    
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.code(short_url, language=None)
                    with col2:
                        if st.button("📋 Copy"):
                            try:
                                pyperclip.copy(short_url)
                                st.success("Copied!")
                            except:
                                st.info("Manual copy needed")
                    
                    # Stats
                    original_length = len(url_input)
                    short_length = len(short_url)
                    reduction = ((original_length - short_length) / original_length) * 100
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Original", f"{original_length} chars")
                    with col2:
                        st.metric("Shortened", f"{short_length} chars")
                    with col3:
                        st.metric("Reduction", f"{reduction:.1f}%")
                        
            except ValueError as e:
                st.error(f"❌ {str(e)}")
            except ConnectionError as e:
                st.error(f"🌐 {str(e)}")
            except Exception as e:
                st.error(f"⚠️ Unexpected error: {str(e)}")
    
    elif shorten_btn:
        st.warning("⚠️ Please enter a URL")
    
    # Footer
    st.markdown("---")
    st.markdown("*Powered by TinyURL API*")

if __name__ == "__main__":
    main()