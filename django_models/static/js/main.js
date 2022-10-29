function eliminarProducto(id) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "Esta acción no se puede revertir",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#dc3545',
        cancelButtonColor: '#212529',
        confirmButtonText: 'Si, eliminar',
        reverseButtons: true,
    })
        .then(function (result) {
            if (result.isConfirmed) {
                window.location.href = "/del_product/" + id + "/"
            }
        })
}