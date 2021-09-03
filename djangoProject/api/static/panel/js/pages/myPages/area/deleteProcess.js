$(document).ready(function () {
    $('#exampleModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const recipient = button.data('whatever');
        const splitText = recipient.toString().split(',');
        const areaName = splitText[0];
        const areaId = (Number)(splitText[1]);
        const LINK = document.getElementById('btn-ok');
        const modal = $(this);
        LINK.href = '/panel/areas/delete/' + areaId + '/';
        modal.find('.modal-body-text').text('¿Seguro que desea eliminar el Área ' + areaName.toString().toUpperCase() + '?')
    })
});

