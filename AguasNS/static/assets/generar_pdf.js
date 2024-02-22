document.addEventListener('DOMContentLoaded', function() {
    const comprarBtn = document.getElementById('comprar-btn');
    
    comprarBtn.addEventListener('click', function() {
        const cantidad = document.getElementById('cantidad').value;
        const codigo = '{{ producto.codigo }}'; // Obtén el código del producto desde el contexto de tu plantilla
        
        // Redirige a la vista que genera el PDF con el código y la cantidad
        window.location.href = `/generar_pdf_boleta/${codigo}/${cantidad}/`;
    });
});
