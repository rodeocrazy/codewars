import pdfrw
from datetime import date


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if type(data_dict[key]) == bool:
                            if data_dict[key] == True:
                                annotation.update(pdfrw.PdfDict(
                                    AS=pdfrw.PdfName('Yes')))
                        else:
                            annotation.update(
                                pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                            )
                            annotation.update(pdfrw.PdfDict(AP=''))
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)
    

# NEW
def fill_simple_pdf_file(data, template_input, template_output):
    some_date = date.today()
    data_dict = {
        'name': data.get('name', ''),
        'phone': data.get('phone', ''),
        'date': some_date,
        'account_number': data.get('account_number', ''),
        'cb_1': data.get('cb_1', False),
        'cb_2': data.get('cb_2', False),
    }
    return fill_pdf(template_input, template_output, data_dict)


if __name__ == '__main__':
    pdf_template = "D:\Google Drive\Learning\Programming\CodeWars\template.pdf"
    pdf_output = "output.pdf"
    
    sample_data_dict = {
        'name': 'Andrew Krcatovich',
        'phone': '(123) 123-1234',
#         'date': date.today(),  # Removed date so we can dynamically set in python.
        'account_number': '123123123',
        'cb_1': True,
        'cb_2': False,
    }
    fill_simple_pdf_file(sample_data_dict, pdf_template, pdf_output)