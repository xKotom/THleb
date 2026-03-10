// Kottom Project - Main JS
document.addEventListener('DOMContentLoaded', function () {
    // Auto-hide messages after 4 seconds
    document.querySelectorAll('.messages__item').forEach(function (el) {
        setTimeout(function () {
            el.style.transition = 'opacity 0.3s';
            el.style.opacity = '0';
            setTimeout(function () { el.remove(); }, 300);
        }, 4000);
    });
});
