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
                career: {
                    validators: {
                        notEmpty: {
                            message: 'Debe seleccionar una carrera obligatoriamente'
                        },
                    }
                },
                yearOfStudy: {
                    validators: {
                        notEmpty: {
                            message: 'Debe seleccionar un año de estudio obligatoriamente'
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


