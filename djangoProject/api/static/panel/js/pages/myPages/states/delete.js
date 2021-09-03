// FUNCTION TO OPEN THE DIALOG COMPONENT
$(document).ready(function () {
    $('#exampleModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const recipient = button.data('whatever');
        const splitText = recipient.toString().split(',');
        const stateName = splitText[0];
        const stateId = (Number)(splitText[1]);
        const LINK = document.getElementById('btn-ok');
        LINK.href = '/panel/states/delete/' + stateId + '/';
        const modal = $(this);
        modal.find('.modal-body-text').text('¿Seguro que desea eliminar el estado ' + stateName.toString().toUpperCase() + '?')
    })
});