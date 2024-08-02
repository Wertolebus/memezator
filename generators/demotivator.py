from PIL import Image, ImageDraw, ImageFont
import json

def read_config() -> dict:
    """Get config var from json file"""
    with open('config.json', 'r') as f:
        return json.load(f)
    
def run(img_fp : str, text1 : str = "", text2 : str = ""):
    imported = Image.open(img_fp)
    
    dem = Image.new(
                    "RGB", 
                    (
                        int(imported.size[0] * 1.7),
                        int(imported.size[1] * 1.7)
                    ),
                    "#000000"
                    )
    
    
    dem.paste(
                imported,
                # idgf why substract by 8 its just working ok
                (
                    (dem.size[0] - imported.size[0]) // 2,
                    (dem.size[1] - imported.size[1]) // 2 - imported.size[1] // 8
                )
            )

    draw = ImageDraw.Draw(dem)
    draw.rectangle(
                    [
                        (
                            (dem.size[0] - imported.size[0]) // 2 - 10,
                            (dem.size[1] - imported.size[1]) // 2 - imported.size[1] // 8 - 10
                        ),
                        (
                            int((imported.size[0]) * 1.35 + 10),
                            int((imported.size[1]) * 1.225 + 10)
                        )
                    ],
                    None,
                    "#ffffff",
                    3
                 )
    
    top_font = ImageFont.truetype(
                                read_config()["font_path"], 
                                int(read_config()["font_size"]),
                            )
    
    bottom_font = ImageFont.truetype(
                                read_config()["font_path"], 
                                int(read_config()["font_size"]) // 2,
                            )
    
    t_text_width = draw.textlength(text1, top_font)
    b_text_width = draw.textlength(text2, bottom_font)
    
    # top text
    draw.text(
                (
                    (dem.size[0] - t_text_width) //2,
                    (imported.size[1] - int(read_config()["font_size"]) // 2) * 1.35
                ),
                text1,
                read_config()["text_color_hex"],
                top_font,
                align='center'
            )
    
    # bottom text
    draw.text(
                (
                    (dem.size[0] - b_text_width) //2,
                    (imported.size[1] - int(read_config()["font_size"]) // 2) * 1.5 + int(read_config()["font_size"]) // 2
                ),
                text2,
                read_config()["text_color_hex"],
                bottom_font,
                align='center'
            )

    dem.show()
