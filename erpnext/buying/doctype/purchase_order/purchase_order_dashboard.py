from frappe import _


def get_data():
	return {
		"fieldname": "purchase_order",
		"non_standard_fieldnames": {
			"Journal Entry": "reference_name",
			"Payment Entry": "reference_name",
			"Payment Request": "reference_name",
			"Auto Repeat": "reference_document",
		},
		"internal_links": {
			"Material Request": ["items", "material_request"],
			"Supplier Quotation": ["items", "supplier_quotation"],
			"Project": ["items", "project"],
		},
		"transactions": [
			{"label": _("Related"), "items": ["Purchase Receipt", "Purchase Invoice", "Purchase Batch Receipt"]},
			{"label": _("Payment"), "items": ["Payment Entry", "Journal Entry", "Payment Request"]},
			{
				"label": _("Reference"),
				"items": ["Material Request", "Supplier Quotation", "Project", "Auto Repeat"],
			},
			{
				"label": _("Sub-contracting"),
				"items": ["Subcontracting Order", "Subcontracting Receipt", "Stock Entry"],
			},
			{"label": _("Internal"), "items": ["Sales Order"]},
		],
	}
