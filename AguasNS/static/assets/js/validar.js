
const cantidadInput = document.getElementById('cantidad');
const stockDisponible = parseInt(document.getElementById('stock_disponible').value, 10);
const stockMessage = document.getElementById('stock_message');

document.getElementById('validar').addEventListener('click', function () {
    const cantidadSeleccionada = parseInt(cantidadInput.value, 10);

    if (cantidadSeleccionada > stockDisponible) {
        stockMessage.style.display = 'block';
    } else {
        stockMessage.style.display = 'none';
    }
});


