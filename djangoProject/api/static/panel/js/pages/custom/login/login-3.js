"use strict";

// Class Definition
var KTLogin = function() {
	var _buttonSpinnerClasses = 'spinner spinner-right spinner-white pr-15';

	var _handleFormSignin = function() {
		var form = KTUtil.getById('kt_login_singin_form');
		var formSubmitUrl = KTUtil.attr(form, 'action');
		var formSubmitButton = KTUtil.getById('kt_login_singin_form_submit_button');

		if (!form) {
			return;
		}


		FormValidation
		    .formValidation(
		        form,
		        {
		            fields: {
						username: {
							validators: {
								notEmpty: {
									message: 'Username is required'
								}
							}
						},
						password: {
							validators: {
								notEmpty: {
									message: 'Password is required'
								}
							}
						}
		            },
		            plugins: {
						trigger: new FormValidation.plugins.Trigger(),
						submitButton: new FormValidation.plugins.SubmitButton(),
	            		defaultSubmit: new FormValidation.plugins.DefaultSubmit(), // Uncomment this line to enable normal button submit after form validation
						bootstrap: new FormValidation.plugins.Bootstrap({
							eleInvalidClass: '', // Repace with uncomment to hide bootstrap validation icons
							eleValidClass: '',   // Repace with uncomment to hide bootstrap validation icons
						})
		            }
		        }
		    )
		    .on('core.form.valid', function() {
				// Show loading state on button
				KTUtil.btnWait(formSubmitButton, _buttonSpinnerClasses, "Please wait");

				// Simulate Ajax request
				setTimeout(function() {
					KTUtil.btnRelease(formSubmitButton);
				}, 2000);

				// Form Validation & Ajax Submission: https://formvalidation.io/guide/examples/using-ajax-to-submit-the-form

		        FormValidation.utils.fetch(formSubmitUrl, {
		            method: 'POST',
					dataType: 'json',
		            params: {
		                name: form.querySelector('[name="username"]').value,
		                email: form.querySelector('[name="password"]').value,
		            },
		        }).then(function(response) { // Return valid JSON
					// Release button
					KTUtil.btnRelease(formSubmitButton);


					if (response && typeof response === 'object' && response.status && response.status === 'success') {
						Swal.fire({
			                text: "All is cool! Now you submit this form",
			                icon: "success",
			                buttonsStyling: false,
							confirmButtonText: "Ok, got it!",
							customClass: {
								confirmButton: "btn font-weight-bold btn-light-primary"
							}
			            }).then(function() {
							KTUtil.scrollTop();
						});
					} else {
						Swal.fire({
			                text: "Sorry, something went wrong, please try again.",
			                icon: "error",
			                buttonsStyling: false,
							confirmButtonText: "Ok, got it!",
							customClass: {
								confirmButton: "btn font-weight-bold btn-light-primary"
							}
			            }).then(function() {
							KTUtil.scrollTop();
						});
					}
		        });

		    })
			.on('core.form.invalid', function() {
				Swal.fire({
					text: "Sorry, looks like there are some errors detected, please try again.",
					icon: "error",
					buttonsStyling: false,
					confirmButtonText: "Ok, got it!",
					customClass: {
						confirmButton: "btn font-weight-bold btn-light-primary"
					}
				}).then(function() {
					KTUtil.scrollTop();
				});
		    });
    }

    // Public Functions
    return {
        init: function() {
            _handleFormSignin();
        }
    };
}();

// Class Initialization
jQuery(document).ready(function() {
    KTLogin.init();
});