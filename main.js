// Initialize Lucide Icons
lucide.createIcons();

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 100,
                behavior: 'smooth'
            });
        }
    });
});

// Dynamic background interaction
document.addEventListener('mousemove', (e) => {
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    
    const glow = document.querySelector('.background-glow');
    glow.style.background = `
        radial-gradient(circle at ${x * 100}% ${y * 100}%, rgba(112, 0, 255, 0.15) 0%, transparent 40%),
        radial-gradient(circle at ${100 - (x * 100)}% ${100 - (y * 100)}%, rgba(0, 242, 255, 0.15) 0%, transparent 40%)
    `;
});

// Reveal animation on scroll
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
        }
    });
}, observerOptions);

document.querySelectorAll('.card').forEach(card => {
    observer.observe(card);
});
