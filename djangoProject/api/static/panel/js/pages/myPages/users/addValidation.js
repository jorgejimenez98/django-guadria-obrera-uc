document.addEventListener('DOMContentLoaded', function (e) {

    FormValidation.validators.noEmptySpaces = function () {
        return {
            validate: function (input) {
                const value = input.value;
                if (value.trim() === '') {
                    return {valid: false}
                }
                return {valid: true}
            }
        }
    };
    FormValidation.validators.strongPassword = function () {
        return {
            validate: function (input) {
                const value = input.value;
                if (value === '') {
                    return {valid: true}
                }
                // COMPROBAR QUE LA CONTRASEÑA TIENE MINUSCULAS
                if (value === value.toUpperCase()) {
                    return {valid: false};
                }
                // COMPROBAR QUE LA CONTRASEÑA TIENE MAYUSCULAS
                if (value === value.toLowerCase()) {
                    return {valid: false};
                }
                // COMPROBAR QUE TIENE DIGITOS
                if (value.search(/[0-9]/) < 0) {
                    return {valid: false}
                }
                return {valid: true}
            }
        }
    }
    const form = document.getElementById('submitForm');
    const fv = FormValidation.formValidation(
        form,
        {
            fields: {
                oldPassword: {
                    validators: {
                        notEmpty: {
                            message: 'La vieja contraseña es obligatoria'
                        },
                    }
                },
                username: {
                    validators: {
                        notEmpty: {
                            message: 'El nombre de usuario es obligatorio'
                        },
                        stringLength: {
                            min: 4,
                            message: 'El nombre de usuario debe tener al menos 4 caracteres.'
                        },
                        noEmptySpaces: {
                            message: 'El nombre de usuario no debe contener espacios en blanco',
                        }
                    }
                },
                names: {
                    validators: {
                        notEmpty: {
                            message: 'El nombre es obligatorio'
                        },
                    }
                },
                lastNames: {
                    validators: {
                        notEmpty: {
                            message: 'Los apellidos son obligatorios'
                        },
                    }
                },
                email: {
                    validators: {
                        notEmpty: {
                            message: 'El Correo es obligatorio'
                        },
                        emailAddress: {
                            message: 'Esta dirección de correo no es correcta'
                        }
                    }
                },
                rol: {
                    validators: {
                        notEmpty: {
                            message: 'Debes seleccionar un rol de usuario',
                        }
                    }
                },
                password: {
                    validators: {
                        notEmpty: {
                            message: 'La contraseña es obligatoria',
                        },
                        stringLength: {
                            min: 6,
                            message: 'La contraseña debe tener al menos 6 caracteres.'
                        },
                        noEmptySpaces: {
                            message: 'La contraseña no debe contener espacios en blanco',
                        },
                        strongPassword: {
                            message: 'La contraseña no es lo suficientemente fuerte.<br>Debe tener mayúsculas, minúsculas y dígitos'
                        }
                    }
                },
                confirmPassword: {
                    validators: {
                        notEmpty: {
                            message: 'Es obligatorio confirmar la contraseña',
                        },
                        identical: {
                            compare: function () {
                                return form.querySelector('[name="password"]').value;
                            },
                            message: 'La contraseña de confirmacion no es igual que la original'
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
    form.querySelector('[name="confirmPassword"]').addEventListener('input', function () {
        fv.revalidateField('confirmPassword');
    })
});


