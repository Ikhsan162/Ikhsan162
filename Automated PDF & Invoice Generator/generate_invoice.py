import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def buat_pdf_invoice(data_invoice, folder_output="output_pdf"):
    """
    Fungsi untuk menghasilkan file PDF Invoice secara otomatis menggunakan ReportLab.
    """
    if not os.path.exists(folder_output):
        os.makedirs(folder_output)
        
    nama_file = f"Invoice_{data_invoice['no_invoice']}.pdf"
    path_file = os.path.join(folder_output, nama_file)
    
    doc = SimpleDocTemplate(path_file, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    style_normal = styles['Normal']
    
    title_style = ParagraphStyle(
        'InvoiceTitle',
        parent=style_normal,
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#1a365d'),
        alignment=2
    )
    
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=style_normal,
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#4a5568')
    )
    
    bold_header = ParagraphStyle(
        'BoldHeader',
        parent=header_style,
        fontName='Helvetica-Bold'
    )

    # --- KEPALA SURAT / HEADER INVOICE ---
    data_header = [
        [
            Paragraph("<b>PT. DINAMIKA GLOBAL KORPORA</b><br/>Jl. Logistik Raya No. 123<br/>Jakarta, Indonesia", header_style),
            Paragraph("INVOICE", title_style)
        ],
        [
            Paragraph("", header_style),
            Paragraph(f"<b>No Invoice:</b> {data_invoice['no_invoice']}<br/><b>Tanggal:</b> {data_invoice['tanggal']}<br/><b>Jatuh Tempo:</b> {data_invoice['jatuh_tempo']}", header_style)
        ]
    ]
    
    t_header = Table(data_header, colWidths=[300, 234])
    t_header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 20))
    
    # --- INFORMASI KLIEN ---
    data_klien = [
        [Paragraph("<b>Kepada Yth:</b>", bold_header)],
        [Paragraph(f"<b>{data_invoice['nama_pelanggan']}</b>", bold_header)],
        [Paragraph(f"{data_invoice['alamat_pelanggan']}", header_style)]
    ]
    t_klien = Table(data_klien, colWidths=[534])
    t_klien.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f7fafc')),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
    ]))
    story.append(t_klien)
    story.append(Spacer(1, 20))
    
    # --- TABEL RINCIAN ITEM ---
    tabel_item = [
        ["Deskripsi Layanan / Produk", "Jumlah", "Harga Satuan", "Total"]
    ]
    
    total_keseluruhan = 0
    for item in data_invoice['items']:
        subtotal = item['jumlah'] * item['harga']
        total_keseluruhan += subtotal
        tabel_item.append([
            item['deskripsi'],
            str(item['jumlah']),
            f"Rp {item['harga']:,.0f}",
            f"Rp {subtotal:,.0f}"
        ])
        
    # Style untuk baris total agar rapi dan rata kanan
    style_label_total = ParagraphStyle(
        'LabelTotal',
        parent=header_style,
        fontName='Helvetica-Bold',
        alignment=2
    )
    
    style_nilai_total = ParagraphStyle(
        'NilaiTotal',
        parent=header_style,
        fontName='Helvetica-Bold',
        alignment=2
    )
    
    label_total = Paragraph("Total Tagihan:", style_label_total)
    nilai_total = Paragraph(f"Rp {total_keseluruhan:,.0f}", style_nilai_total)
    
    # Menambahkan baris total (menggunakan string kosong untuk kolom yang digabungkan)
    tabel_item.append(["", "", label_total, nilai_total])
    
    t_rincian = Table(tabel_item, colWidths=[234, 70, 110, 120])
    t_rincian.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2b6cb0')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 10),
        ('ALIGN', (1,1), (-1,-1), 'CENTER'),
        ('ALIGN', (3,1), (3,-1), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('TOPPADDING', (0,0), (-1,0), 8),
        ('GRID', (0,0), (-1,-2), 0.5, colors.HexColor('#cbd5e0')),
        ('BACKGROUND', (2,-1), (3,-1), colors.HexColor('#edf2f7')),
        ('LINEABOVE', (2,-1), (3,-1), 1, colors.HexColor('#2b6cb0')),
        ('PADDING', (0,1), (-1,-1), 6),
        ('SPAN', (0, -1), (1, -1)),  # Menggabungkan kolom deskripsi & jumlah untuk baris total
    ]))
    story.append(t_rincian)
    story.append(Spacer(1, 40))
    
    # --- CATATAN & TANDA TANGAN ---
    data_ttd = [
        [
            Paragraph("<b>Catatan:</b><br/>Pembayaran dapat ditransfer melalui Rekening Bank BCA a.n PT Dinamika Global Korpora No. 1234567890.", header_style),
            Paragraph("Hormat Kami,<br/><br/><br/><b>Manajemen Keuangan</b>", ParagraphStyle('Ttd', parent=header_style, alignment=1))
        ]
    ]
    t_ttd = Table(data_ttd, colWidths=[334, 200])
    t_ttd.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_ttd)
    
    doc.build(story)
    print(f"[Sukses] Berhasil membuat PDF: {path_file}")