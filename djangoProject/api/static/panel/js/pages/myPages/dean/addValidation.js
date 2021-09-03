document.addEventListener('DOMContentLoaded', function (e) {
    const form = document.getElementById('submitForm');
    const fv = FormValidation.formValidation(
        form,
        {
            fields: {
                user: {
                    validators: {
                        notEmpty: {
                            message: 'Debe seleccionar un usuario obligatoriamente'
                        },
                    }
                },
                faculty: {
                    validators: {
                        notEmpty: {
                            message: 'Debe seleccionar una facultad obligatoriamente'
                        },
                    }
                },

            },

            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                // Bootstrap Framework Integration
                bootstrap: new FormValidation.plugins.Bootstrap(),
                // Validate fields when clicking the Submit button
                submitButton: new FormValidation.plugins.SubmitButton(),
                // Submit the form when all fields are valid
                defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
            }
        }
    );

});


