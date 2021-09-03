// FUNCTION TO OPEN THE DIALOG COMPONENT
$(document).ready(function () {
    $('#exampleModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const recipient = button.data('whatever');
        const splitText = recipient.toString().split(',');
        const career = splitText[0];
        const careerId = (Number)(splitText[1]);
        const faculty = splitText[2];
        const LINK = document.getElementById('btn-ok');
        LINK.href = '/panel/careers/delete/' + careerId + '/';
        const modal = $(this);
        modal.find('.modal-body-text').text('¿Seguro que desea eliminar la carrera ' + career.toUpperCase() + ' de la facultad de ' + faculty +'?')
    })
});