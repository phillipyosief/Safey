from dearpygui.core import *
from assets import properties
import json

def main():
    set_main_window_title(f'{properties.ProductName}')
    set_main_window_size(1308, 759)

def check_theme_on_startup():
    with open('user/settings.hqs', 'r') as settings:
        theme = json.load(settings)

        if theme["theme"] == 'Dark':
            DefaultTheme()
        elif theme["theme"] == 'dark':
            DefaultTheme()
        elif theme["theme"] == 'Default':
            DefaultTheme()
        elif theme["theme"] == 'default':
            DefaultTheme()
        elif theme["theme"] == 'None':
            DefaultTheme()
        else:
            try:
                set_theme(theme["theme"])
                style()
            except:
                DefaultTheme()

def style():
    add_additional_font(properties.DefaultFont, 15, custom_glyph_chars=[[0x00C1, 0x00C3], [0x00C4, 0x00C8]])
    
    set_style_window_padding(8.00, 8.00)
    set_style_frame_padding(4.00, 3.00)
    set_style_item_spacing(8.00, 4.00)
    set_style_item_inner_spacing(4.00, 4.00)
    set_style_touch_extra_padding(0.00, 0.00)
    set_style_indent_spacing(21.00)
    set_style_scrollbar_size(14.00)
    set_style_grab_min_size(10.00)
    set_style_window_border_size(1.00)
    set_style_child_border_size(1.00)
    set_style_popup_border_size(1.00)
    set_style_frame_border_size(0.00)
    set_style_tab_border_size(0.00)
    set_style_window_rounding(7.00)
    set_style_child_rounding(0.00)
    set_style_frame_rounding(2.00)
    set_style_popup_rounding(0.00)
    set_style_scrollbar_rounding(9.00)
    set_style_grab_rounding(2.00)
    set_style_tab_rounding(4.00)
    set_style_window_title_align(0.00, 0.50)
    set_style_window_menu_button_position(mvDir_Left)
    set_style_color_button_position(mvDir_Right)
    set_style_button_text_align(0.50, 0.50)
    set_style_selectable_text_align(0.00, 0.00)
    set_style_display_safe_area_padding(3.00, 3.00)
    set_style_global_alpha(1.00)
    set_style_antialiased_lines(True)
    set_style_antialiased_fill(True)
    set_style_curve_tessellation_tolerance(1.25)
    set_style_circle_segment_max_error(1.60)

def colors():
    set_theme_item(mvGuiCol_Text, 255, 255, 255, 255)
    set_theme_item(mvGuiCol_TextDisabled, 128, 128, 128, 255)
    set_theme_item(mvGuiCol_WindowBg, 15, 15, 15, 240)
    set_theme_item(mvGuiCol_PopupBg, 20, 20, 20, 240)
    set_theme_item(mvGuiCol_Border, 110, 110, 128, 128)
    set_theme_item(mvGuiCol_FrameBg, 49, 49, 49, 138)
    set_theme_item(mvGuiCol_FrameBgHovered, 41, 41, 41, 138)
    set_theme_item(mvGuiCol_FrameBgActive, 37, 36, 36, 138)
    set_theme_item(mvGuiCol_TitleBg, 10, 10, 10, 255)
    set_theme_item(mvGuiCol_TitleBgActive, 23, 23, 23, 255)
    set_theme_item(mvGuiCol_TitleBgCollapsed, 0, 0, 0, 130)
    set_theme_item(mvGuiCol_MenuBarBg, 36, 36, 36, 255)
    set_theme_item(mvGuiCol_ScrollbarBg, 5, 5, 5, 135)
    set_theme_item(mvGuiCol_ScrollbarGrab, 30, 30, 30, 255)
    set_theme_item(mvGuiCol_ScrollbarGrabHovered, 31, 31, 31, 255)
    set_theme_item(mvGuiCol_ScrollbarGrabActive, 32, 32, 32, 255)
    set_theme_item(mvGuiCol_CheckMark, 139, 139, 139, 255)
    set_theme_item(mvGuiCol_SliderGrab, 86, 86, 86, 255)
    set_theme_item(mvGuiCol_SliderGrabActive, 52, 52, 52, 255)
    set_theme_item(mvGuiCol_Button, 114, 114, 114, 102)
    set_theme_item(mvGuiCol_ButtonHovered, 99, 99, 99, 102)
    set_theme_item(mvGuiCol_ButtonActive, 85, 85, 85, 102)
    set_theme_item(mvGuiCol_Header, 87, 87, 87, 79)
    set_theme_item(mvGuiCol_HeaderHovered, 70, 70, 70, 204)
    set_theme_item(mvGuiCol_HeaderActive, 62, 62, 62, 255)
    set_theme_item(mvGuiCol_Separator, 110, 110, 128, 128)
    set_theme_item(mvGuiCol_SeparatorHovered, 89, 89, 89, 199)
    set_theme_item(mvGuiCol_SeparatorActive, 62, 62, 62, 255)
    set_theme_item(mvGuiCol_ResizeGrip, 130, 130, 130, 64)
    set_theme_item(mvGuiCol_ResizeGripHovered, 99, 99, 99, 171)
    set_theme_item(mvGuiCol_ResizeGripActive, 113, 113, 113, 242)
    set_theme_item(mvGuiCol_Tab, 56, 56, 56, 220)
    set_theme_item(mvGuiCol_TabHovered, 73, 73, 73, 204)
    set_theme_item(mvGuiCol_TabActive, 82, 82, 82, 255)
    set_theme_item(mvGuiCol_TabUnfocused, 17, 26, 38, 248)
    set_theme_item(mvGuiCol_TabUnfocusedActive, 35, 67, 108, 255)
    set_theme_item(mvGuiCol_PlotLines, 156, 156, 156, 255)
    set_theme_item(mvGuiCol_PlotLinesHovered, 255, 110, 89, 255)
    set_theme_item(mvGuiCol_TextSelectedBg, 66, 150, 250, 89)
    set_theme_item(mvGuiCol_NavHighlight, 66, 150, 250, 255)
    set_theme_item(mvGuiCol_ModalWindowDimBg, 204, 204, 204, 89)

def DefaultTheme():
    style()
    colors()


