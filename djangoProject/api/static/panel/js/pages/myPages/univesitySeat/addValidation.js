document.addEventListener('DOMContentLoaded', function (e) {

    FormValidation.validators.isValidNumber = function () {
        return {
            validate: function (input) {
                const value = input.value;
                if (value >= 1 && value <= 10) {
                    return {valid: true}
                }
                return {valid: false}
            }
        }
    };
    const form = document.getElementById('submitForm');
    const fv = FormValidation.formValidation(
        form,
        {
            fields: {
                name: {
                    validators: {
                        notEmpty: {
                            message: 'El nombre de la Sede Universitaria es obligatorio'
                        },
                    }
                },
                cantAOGS: {
                    validators: {
                        isValidNumber: {
                            message: 'La cantidad de AOGS deben ser entre 1 y 10'
                        }
                    }
                }
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



