$(document).ready(function () {
        FormValidation.formValidation(
            document.getElementById('submitForm'),
            {
                fields: {
                    name: {
                        validators: {
                            notEmpty: {
                                message: 'El nombre del estado es obligatorio'
                            },
                        }
                    },
                    typeOfPerson: {
						validators: {
							notEmpty: {
								message: 'Debe seleccionar un tipo de persona',
							}
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
            })
    }
);