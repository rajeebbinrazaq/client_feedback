frappe.ready(function() {
	// bind events here

	frappe.web_form.after_load = () => {
		// init script here
		frappe.web_form.validate = () => {
			let data = frappe.web_form.get_values();
			if (!data.client_email_id.includes('@')) {
				frappe.msgprint('Please enter a valid email id');
				return false;
			}
			return true;
		};	
	}
});