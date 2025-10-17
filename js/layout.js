// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {

    // Funcionalidad del menú móvil
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const closeSidebarButton = document.getElementById('close-sidebar');
    const mobileSidebar = document.getElementById('mobile-sidebar');

    if (mobileMenuButton && mobileSidebar) {
        mobileMenuButton.addEventListener('click', () => {
            mobileSidebar.classList.remove('hidden');
        });
    }

    if (closeSidebarButton && mobileSidebar) {
        closeSidebarButton.addEventListener('click', () => {
            mobileSidebar.classList.add('hidden');
        });
    }

    // Funcionalidad de los elementos del menú
    const menuItems = document.querySelectorAll('.sidebar-item');
    if (menuItems.length > 0) {
        menuItems.forEach(item => {
            item.addEventListener('click', () => {
                // Remover la clase 'active' de todos los elementos
                menuItems.forEach(i => i.classList.remove('active'));

                // Añadir la clase 'active' al elemento clickeado
                item.classList.add('active');
            });
        });
    }

});