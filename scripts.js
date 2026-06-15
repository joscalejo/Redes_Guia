document.addEventListener('DOMContentLoaded', () => {
    // Accordion Logic
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const content = this.nextElementSibling;
            const isActive = this.classList.contains('active');
            const parentCard = this.closest('.card');
            if (parentCard) {
                const allHeadersInCard = parentCard.querySelectorAll('.accordion-header');
                allHeadersInCard.forEach(h => {
                    h.classList.remove('active');
                    if (h.nextElementSibling) h.nextElementSibling.style.maxHeight = null;
                });
            }
            if (!isActive) {
                this.classList.add('active');
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });

    // Init first accordions as open
    document.querySelectorAll('.module-section').forEach(section => {
        const firstHeader = section.querySelector('.accordion-header');
        if (firstHeader) {
            firstHeader.classList.add('active');
            const content = firstHeader.nextElementSibling;
            if (content) {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        }
    });

    // Mobile Menu
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    function toggleMenu() {
        sidebar.classList.toggle('show');
        overlay.classList.toggle('show');
    }
    if (menuToggle) menuToggle.addEventListener('click', toggleMenu);
    if (overlay) overlay.addEventListener('click', toggleMenu);

    document.querySelectorAll('.sidebar-nav .nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 992) toggleMenu();
        });
    });

    // Scrollspy
    const sections = document.querySelectorAll('.module-section');
    const navLinks = document.querySelectorAll('.sidebar-nav .nav-link');
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            if (window.scrollY >= (section.offsetTop - 300)) {
                current = section.getAttribute('id');
            }
        });
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (current && link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    });
});
