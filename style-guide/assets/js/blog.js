document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Reading Progress Bar
    const progressBar = document.getElementById('reading-progress');
    const articleContent = document.getElementById('blog-content-body');
    
    if (progressBar && articleContent) {
        window.addEventListener('scroll', () => {
            const articleRect = articleContent.getBoundingClientRect();
            const articleTop = articleRect.top + window.scrollY;
            const articleHeight = articleRect.height;
            const windowHeight = window.innerHeight;
            
            // Calculate progress based on scroll position relative to article
            let progress = 0;
            const scrollY = window.scrollY;
            
            // If we're past the start of the article
            if (scrollY > articleTop - windowHeight / 2) {
                const scrolled = scrollY - (articleTop - windowHeight / 2);
                const totalScrollable = articleHeight;
                progress = (scrolled / totalScrollable) * 100;
            }
            
            // Clamp between 0 and 100
            progress = Math.max(0, Math.min(100, progress));
            progressBar.style.width = `${progress}%`;
        });
    }
    
    // 2. Table of Contents Highlighting
    const tocLinks = document.querySelectorAll('.blog-toc-list a');
    const headings = document.querySelectorAll('.blog-content h2, .blog-content h3');
    
    if (tocLinks.length > 0 && headings.length > 0) {
        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -60% 0px',
            threshold: 1.0
        };
        
        let activeId = null;
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    activeId = entry.target.id;
                }
            });
            
            // Update classes
            tocLinks.forEach(link => {
                const href = link.getAttribute('href').substring(1);
                if (href === activeId) {
                    link.classList.add('is-active');
                } else {
                    link.classList.remove('is-active');
                }
            });
        }, observerOptions);
        
        headings.forEach(heading => {
            if (heading.id) {
                observer.observe(heading);
            }
        });
        
        // Smooth scroll for TOC links
        tocLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href').substring(1);
                const targetEl = document.getElementById(targetId);
                if (targetEl) {
                    window.scrollTo({
                        top: targetEl.offsetTop - 120, // offset for fixed header
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    // 3. Code Copy Buttons
    const copyBtns = document.querySelectorAll('.blog-copy-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-clipboard-target');
            const targetCode = document.querySelector(targetId);
            
            if (targetCode) {
                navigator.clipboard.writeText(targetCode.innerText).then(() => {
                    const originalText = btn.innerText;
                    btn.innerText = 'Copied!';
                    setTimeout(() => {
                        btn.innerText = originalText;
                    }, 2000);
                });
            }
        });
    });

    // 4. FAQ Accordions
    const faqQuestions = document.querySelectorAll('.blog-faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;
            const isOpen = question.classList.contains('is-open');
            
            // Close all others
            faqQuestions.forEach(q => {
                q.classList.remove('is-open');
                q.nextElementSibling.style.maxHeight = null;
            });
            
            if (!isOpen) {
                question.classList.add('is-open');
                answer.style.maxHeight = answer.scrollHeight + "px";
            }
        });
    });

});
