// FUNCTION TO OPEN THE DIALOG COMPONENT
$(document).ready(function () {
    $('#exampleModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const recipient = button.data('whatever');
        const splitText = recipient.toString().split(',');
        const user = splitText[0];
        const userId = (Number)(splitText[1]);
        const LINK = document.getElementById('btn-ok');
        LINK.href = '/panel/users/programmerFaculty/delete/' + userId + '/';
        const modal = $(this);
        modal.find('.modal-body-text').text('¿Seguro que desea eliminar el Programador de la guardia (' + user + ')?')
    })
});