/* AcrenKey Property Detail Page Interactive Controller */

document.addEventListener('DOMContentLoaded', function() {
  
  // 1. Gallery Thumbnail Switching
  var mainImg = document.getElementById('propMainImage');
  var thumbs = document.querySelectorAll('.prop-thumb-item');
  
  thumbs.forEach(function(thumb) {
    thumb.addEventListener('click', function() {
      var fullUrl = this.getAttribute('data-full');
      if (fullUrl && mainImg) {
        mainImg.src = fullUrl;
        thumbs.forEach(function(t) { t.classList.remove('active'); });
        this.classList.add('active');
      }
    });
  });

  // 2. Floor Plan Tab Switching
  var fpTabs = document.querySelectorAll('.prop-fp-tab-btn');
  var fp3bhk = document.getElementById('fp-content-3bhk');
  var fp4bhk = document.getElementById('fp-content-4bhk');

  fpTabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      var target = this.getAttribute('data-tab');
      fpTabs.forEach(function(t) { t.classList.remove('active'); });
      this.classList.add('active');

      if (target === '3bhk') {
        if (fp3bhk) fp3bhk.style.display = 'grid';
        if (fp4bhk) fp4bhk.style.display = 'none';
      } else if (target === '4bhk') {
        if (fp3bhk) fp3bhk.style.display = 'none';
        if (fp4bhk) fp4bhk.style.display = 'grid';
      }
    });
  });

  // 3. FAQ Accordion Toggle
  var faqItems = document.querySelectorAll('.prop-faq-item');
  faqItems.forEach(function(item) {
    var q = item.querySelector('.prop-faq-q');
    if (q) {
      q.addEventListener('click', function() {
        var isOpen = item.classList.contains('active');
        faqItems.forEach(function(i) { i.classList.remove('active'); });
        if (!isOpen) {
          item.classList.add('active');
        }
      });
    }
  });

  // 4. Section Navigation Active State on Scroll
  var sections = document.querySelectorAll('.prop-section, .prop-hero-section');
  var navLinks = document.querySelectorAll('.prop-nav-link');

  window.addEventListener('scroll', function() {
    var fromTop = window.scrollY + 120;

    sections.forEach(function(sec) {
      var id = sec.getAttribute('id');
      if (!id) return;

      if (sec.offsetTop <= fromTop && (sec.offsetTop + sec.offsetHeight) > fromTop) {
        navLinks.forEach(function(link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  });

  // 5. Smooth Scroll for Section Nav Links
  navLinks.forEach(function(link) {
    link.addEventListener('click', function(e) {
      var href = this.getAttribute('href');
      if (href && href.startsWith('#')) {
        var targetEl = document.querySelector(href);
        if (targetEl) {
          e.preventDefault();
          var offsetTop = targetEl.offsetTop - 100;
          window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
          });
        }
      }
    });
  });

});


  // 6. Amenities Drawer Overlay Controls
  var amDrawer = document.getElementById('propAmenitiesDrawer');
  var amCloseBtn = document.getElementById('propDrawerClose');

  window.openAmenitiesDrawer = function() {
    if (amDrawer) {
      amDrawer.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeAmenitiesDrawer = function() {
    if (amDrawer) {
      amDrawer.classList.remove('active');
      document.body.style.overflow = '';
    }
  };

  if (amCloseBtn) {
    amCloseBtn.addEventListener('click', window.closeAmenitiesDrawer);
  }

  if (amDrawer) {
    amDrawer.addEventListener('click', function(e) {
      if (e.target === amDrawer) {
        window.closeAmenitiesDrawer();
      }
    });
  }
