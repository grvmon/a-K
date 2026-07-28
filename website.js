document.addEventListener('DOMContentLoaded', function () {
    // 1. Initialize Feather Icons
    if (typeof feather !== 'undefined') {
        feather.replace();
    }

    // 2. Header Scroll Effect
    const headerNav = document.getElementById('header-nav');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 30) {
            headerNav.classList.add('scrolled');
        } else {
            headerNav.classList.remove('scrolled');
        }
    });

    // 3. Mobile Menu Toggle
    const mobileBtn = document.getElementById('mobile-toggle-btn');
    const mobileDrawer = document.getElementById('mobile-drawer');

    if (mobileBtn && mobileDrawer) {
        mobileBtn.addEventListener('click', function () {
            mobileDrawer.classList.toggle('active');
        });

        // Close mobile menu on link click
        const drawerLinks = mobileDrawer.querySelectorAll('a');
        drawerLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                mobileDrawer.classList.remove('active');
            });
        });
    }
});
