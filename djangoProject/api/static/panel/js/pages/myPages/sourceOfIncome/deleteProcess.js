// FUNCTION TO OPEN THE DIALOG COMPONENT
$(document).ready(function () {
    $('#exampleModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const recipient = button.data('whatever');
        const splitText = recipient.toString().split(',');
        const typeOfStudent = splitText[0];
        const idSourceOfIncome = (Number)(splitText[1]);
        const LINK = document.getElementById('btn-ok');
        LINK.href = '/panel/sourceOfIncomes/delete/' + idSourceOfIncome + '/';
        const modal = $(this);
        modal.find('.modal-body-text').text('¿Seguro que desea eliminar la fuente de ingreso (' + typeOfStudent.toUpperCase() + ')?')
    })
});