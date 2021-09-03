$(document).ready(function () {
        FormValidation.formValidation(
            document.getElementById('submitForm'),
            {
                fields: {
                    name: {
                        validators: {
                            notEmpty: {
                                message: 'El nombre del departamento es obligatorio'
                            },
                        }
                    },
                    areaName: {
						validators: {
							notEmpty: {
								message: 'Debe seleccionar un area para el departamento',
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