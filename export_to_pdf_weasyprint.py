"""
将 main.html 导出为 PDF 作品集的脚本（使用 WeasyPrint）
如果 playwright 安装有问题，可以使用这个版本
"""

from pathlib import Path
from weasyprint import HTML, CSS
from urllib.parse import urljoin, urlparse
import os


def export_html_to_pdf():
    """将 HTML 文件导出为 PDF"""
    
    # 获取当前脚本所在目录
    script_dir = Path(__file__).parent.absolute()
    html_file = script_dir / "main.html"
    output_pdf = script_dir / "portfolio.pdf"
    
    # 检查 HTML 文件是否存在
    if not html_file.exists():
        print(f"错误: 找不到文件 {html_file}")
        return
    
    print(f"正在将 {html_file} 导出为 PDF...")
    
    try:
        # 读取 HTML 文件
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 将 HTML 转换为 PDF
        print("正在生成 PDF...")
        
        # 使用 WeasyPrint 生成 PDF
        HTML(string=html_content, base_url=str(script_dir)).write_pdf(
            output_pdf,
            stylesheets=[
                CSS(string='''
                    @page {
                        size: A4;
                        margin: 20mm 15mm;
                    }
                    body {
                        font-family: Arial, sans-serif;
                    }
                    /* 隐藏一些不适合打印的元素 */
                    .alert_bar {
                        display: none !important;
                    }
                    .photo-wall-container {
                        page-break-inside: avoid;
                    }
                    /* 确保图片不会超出页面 */
                    img {
                        max-width: 100%;
                        height: auto;
                    }
                ''')
            ]
        )
        
        print(f"✅ PDF 已成功导出到: {output_pdf}")
        print(f"文件大小: {output_pdf.stat().st_size / 1024 / 1024:.2f} MB")
        
    except ImportError:
        print("错误: 未安装 weasyprint 库")
        print("请运行以下命令安装:")
        print("  pip install weasyprint")
    except Exception as e:
        print(f"导出过程中出现错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    export_html_to_pdf()


