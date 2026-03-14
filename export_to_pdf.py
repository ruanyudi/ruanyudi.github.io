"""
将 main.html 导出为 PDF 作品集的脚本
使用 Playwright 来渲染网页并导出为 PDF
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
import os


async def export_html_to_pdf():
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
    
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=True)
        
        # 创建新页面
        page = await browser.new_page()
        
        # 将 HTML 文件路径转换为 file:// URL
        html_path = html_file.as_uri()
        
        print(f"正在加载页面: {html_path}")
        
        # 加载 HTML 文件
        await page.goto(html_path, wait_until="networkidle")
        
        # 等待页面完全加载（包括图片和样式）
        await page.wait_for_timeout(2000)  # 等待 2 秒确保所有资源加载完成
        
        # 设置 PDF 选项
        pdf_options = {
            "path": str(output_pdf),
            "format": "A4",
            "print_background": True,  # 包含背景颜色和图片
            "margin": {
                "top": "20mm",
                "right": "15mm",
                "bottom": "20mm",
                "left": "15mm"
            },
            "prefer_css_page_size": False,
            "display_header_footer": False,
        }
        
        print("正在生成 PDF...")
        
        # 导出为 PDF
        await page.pdf(**pdf_options)
        
        # 关闭浏览器
        await browser.close()
        
        print(f"✅ PDF 已成功导出到: {output_pdf}")
        print(f"文件大小: {output_pdf.stat().st_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    try:
        asyncio.run(export_html_to_pdf())
    except ImportError:
        print("错误: 未安装 playwright 库")
        print("请运行以下命令安装:")
        print("  pip install playwright")
        print("  playwright install chromium")
    except Exception as e:
        print(f"导出过程中出现错误: {e}")
        import traceback
        traceback.print_exc()


