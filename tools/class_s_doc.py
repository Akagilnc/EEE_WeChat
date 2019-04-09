import json
from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
from pprint import pprint


def iter_block_items(parent):
    """
    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
        # print(parent_elm.xml)
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


doc = Document('./5th_class_s.docx')
classes = []
for block in iter_block_items(doc):
    if not isinstance(block, Paragraph):
        for row in block.rows:
            if len(row.cells) > 2:
                classes.append([cell.text.replace(' ', '').replace('\n', ' ').strip() for cell in row.cells])

results = []
titles = []
for i in range(len(classes)):
    if i == 0:
        titles = classes[i][:3]
        continue
    result = {"time": classes[i][0]}
    teacher = classes[i][1].split(" ", maxsplit=1)
    if len(teacher) == 2:
        result["teacher"] = {"name": teacher[0], "title": teacher[1]}
    result["title"] = classes[i][2]
    result["type"] = classes[i][3]
    result["address"] = classes[i][4]
    results.append(result)

with open('index.json', 'w', encoding='utf-8') as file:
    results_json = {'titles': [{'title': item} for item in titles], 'classes': results}
    json.dump([results_json], file, ensure_ascii=False)


