// Copyright (c) 2020, mvit ise and contributors
// For license information, please see license.txt

frappe.ui.form.on('Department Placement Report', {
	company: function (frm,cdt,cdn){
		var placement= frappe.model.get_doc(cdt,cdn);
		frm.call({
			doc:frm.doc,
			method:"get_usn",
			args:{
				department:placement.department,
				company:placement.company
			}
		})
	}	
});
