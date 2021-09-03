"use strict";

// Class definition

function showModal() {
    $('#exampleModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const recipient = button.data('whatever');
        const splitText = recipient.toString().split(',');
        const areaName = splitText[0];
        const areaId = (Number)(splitText[1]);
        const LINK = document.getElementById('btn-ok');
        LINK.href = '/panel/areas/delete/' + areaId + '/';
        const modal = $(this);
        modal.find('.modal-body-text').text('¿Seguro que desea eliminar el Área ' + areaName.toString().toUpperCase() + '?')
    })
}

var KTBootstrapNotifyDemo = function () {

    // Private functions

    // basic demo
    var demo = function () {
        // init bootstrap switch
        showModal();
        $('[data-switch=true]').bootstrapSwitch();

        // handle the demo
        $('#btn-ok').click(function () {
            var content = {};

            content.message = 'Nueva area ha sido ingresada';
            content.title = 'Insertar Area';
            content.icon = 'icon ' + 'la la-warning';
            content.target = '_blank';

            var notify = $.notify(content, {
                type: 'Success',
                allow_dismiss: true,
                newest_on_top: true,
                mouse_over: true,
                showProgressbar: true,
                spacing: 10,
                timer: 2000,
                placement: {
                    from: 'Top',
                    align: 'Right'
                },
                offset: {
                    x: 21,
                    y: 30
                },
                delay: 1000,
                z_index: 10000,
                animate: {
                    enter: 'animate__animated animate__jello',
                    exit: 'animate__animated animate__jello'
                }
            });

            setTimeout(function () {
                notify.update('message', '<strong>Guardando</strong> datos de la pagina.');
                notify.update('type', 'primary');
                notify.update('progress', 20);
            }, 1000);

            setTimeout(function () {
                notify.update('message', '<strong>Guardiando</strong> Datos del usuario.');
                notify.update('type', 'warning');
                notify.update('progress', 40);
            }, 2000);

            setTimeout(function () {
                notify.update('message', '<strong>Guardando</strong> Datos del perfil.');
                notify.update('type', 'danger');
                notify.update('progress', 65);
            }, 3000);

            setTimeout(function () {
                notify.update('message', '<strong>Checkeando</strong> errores.');
                notify.update('type', 'success');
                notify.update('progress', 100);
            }, 4000);
        });
    }

    return {
        // public functions
        init: function () {
            demo();
        }
    };
}();

jQuery(document).ready(function () {
    KTBootstrapNotifyDemo.init();
});
