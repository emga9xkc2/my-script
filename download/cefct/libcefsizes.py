from .libcefdef import *
from .libcefinternal import *
from .libcefstruct import *

cefsizesok = 1
def cefchecksize(name, t, size):
    if sizeof(t) != size:
        print("sizeof({}) = {} != {}".format(name, sizeof(t), size))
        return 0
    return 1
cefsizesok &= cefchecksize("cef_accessibility_handler_t", cef_accessibility_handler_t, 56)
cefsizesok &= cefchecksize("cef_app_t", cef_app_t, 80)
cefsizesok &= cefchecksize("cef_audio_handler_t", cef_audio_handler_t, 80)
cefsizesok &= cefchecksize("cef_auth_callback_t", cef_auth_callback_t, 56)
cefsizesok &= cefchecksize("cef_before_download_callback_t", cef_before_download_callback_t, 48)
cefsizesok &= cefchecksize("cef_binary_value_t", cef_binary_value_t, 96)
cefsizesok &= cefchecksize("cef_box_layout_t", cef_box_layout_t, 80)
cefsizesok &= cefchecksize("cef_browser_host_t", cef_browser_host_t, 512)
cefsizesok &= cefchecksize("cef_browser_process_handler_t", cef_browser_process_handler_t, 80)
cefsizesok &= cefchecksize("cef_browser_t", cef_browser_t, 208)
cefsizesok &= cefchecksize("cef_browser_view_delegate_t", cef_browser_view_delegate_t, 160)
cefsizesok &= cefchecksize("cef_browser_view_t", cef_browser_view_t, 464)
cefsizesok &= cefchecksize("cef_button_delegate_t", cef_button_delegate_t, 136)
cefsizesok &= cefchecksize("cef_button_t", cef_button_t, 488)
cefsizesok &= cefchecksize("cef_callback_t", cef_callback_t, 56)
cefsizesok &= cefchecksize("cef_client_t", cef_client_t, 192)
cefsizesok &= cefchecksize("cef_command_handler_t", cef_command_handler_t, 48)
cefsizesok &= cefchecksize("cef_command_line_t", cef_command_line_t, 200)
cefsizesok &= cefchecksize("cef_completion_callback_t", cef_completion_callback_t, 48)
cefsizesok &= cefchecksize("cef_context_menu_handler_t", cef_context_menu_handler_t, 96)
cefsizesok &= cefchecksize("cef_context_menu_params_t", cef_context_menu_params_t, 200)
cefsizesok &= cefchecksize("cef_cookie_access_filter_t", cef_cookie_access_filter_t, 56)
cefsizesok &= cefchecksize("cef_cookie_manager_t", cef_cookie_manager_t, 80)
cefsizesok &= cefchecksize("cef_cookie_visitor_t", cef_cookie_visitor_t, 48)
cefsizesok &= cefchecksize("cef_delete_cookies_callback_t", cef_delete_cookies_callback_t, 48)
cefsizesok &= cefchecksize("cef_dev_tools_message_observer_t", cef_dev_tools_message_observer_t, 80)
cefsizesok &= cefchecksize("cef_dialog_handler_t", cef_dialog_handler_t, 48)
cefsizesok &= cefchecksize("cef_dictionary_value_t", cef_dictionary_value_t, 272)
cefsizesok &= cefchecksize("cef_display_handler_t", cef_display_handler_t, 128)
cefsizesok &= cefchecksize("cef_display_t", cef_display_t, 96)
cefsizesok &= cefchecksize("cef_domdocument_t", cef_domdocument_t, 152)
cefsizesok &= cefchecksize("cef_domnode_t", cef_domnode_t, 248)
cefsizesok &= cefchecksize("cef_domvisitor_t", cef_domvisitor_t, 48)
cefsizesok &= cefchecksize("cef_download_handler_t", cef_download_handler_t, 64)
cefsizesok &= cefchecksize("cef_download_image_callback_t", cef_download_image_callback_t, 48)
cefsizesok &= cefchecksize("cef_download_item_callback_t", cef_download_item_callback_t, 64)
cefsizesok &= cefchecksize("cef_download_item_t", cef_download_item_t, 176)
cefsizesok &= cefchecksize("cef_drag_data_t", cef_drag_data_t, 248)
cefsizesok &= cefchecksize("cef_drag_handler_t", cef_drag_handler_t, 56)
cefsizesok &= cefchecksize("cef_end_tracing_callback_t", cef_end_tracing_callback_t, 48)
cefsizesok &= cefchecksize("cef_extension_handler_t", cef_extension_handler_t, 104)
cefsizesok &= cefchecksize("cef_extension_t", cef_extension_t, 104)
cefsizesok &= cefchecksize("cef_file_dialog_callback_t", cef_file_dialog_callback_t, 56)
cefsizesok &= cefchecksize("cef_fill_layout_t", cef_fill_layout_t, 64)
cefsizesok &= cefchecksize("cef_find_handler_t", cef_find_handler_t, 48)
cefsizesok &= cefchecksize("cef_focus_handler_t", cef_focus_handler_t, 64)
cefsizesok &= cefchecksize("cef_frame_handler_t", cef_frame_handler_t, 72)
cefsizesok &= cefchecksize("cef_frame_t", cef_frame_t, 240)
cefsizesok &= cefchecksize("cef_get_extension_resource_callback_t", cef_get_extension_resource_callback_t, 56)
cefsizesok &= cefchecksize("cef_image_t", cef_image_t, 144)
cefsizesok &= cefchecksize("cef_jsdialog_callback_t", cef_jsdialog_callback_t, 48)
cefsizesok &= cefchecksize("cef_jsdialog_handler_t", cef_jsdialog_handler_t, 72)
cefsizesok &= cefchecksize("cef_keyboard_handler_t", cef_keyboard_handler_t, 56)
cefsizesok &= cefchecksize("cef_label_button_t", cef_label_button_t, 576)
cefsizesok &= cefchecksize("cef_layout_t", cef_layout_t, 64)
cefsizesok &= cefchecksize("cef_life_span_handler_t", cef_life_span_handler_t, 72)
cefsizesok &= cefchecksize("cef_list_value_t", cef_list_value_t, 264)
cefsizesok &= cefchecksize("cef_load_handler_t", cef_load_handler_t, 72)
cefsizesok &= cefchecksize("cef_media_access_callback_t", cef_media_access_callback_t, 56)
cefsizesok &= cefchecksize("cef_media_observer_t", cef_media_observer_t, 72)
cefsizesok &= cefchecksize("cef_media_route_create_callback_t", cef_media_route_create_callback_t, 48)
cefsizesok &= cefchecksize("cef_media_route_t", cef_media_route_t, 80)
cefsizesok &= cefchecksize("cef_media_router_t", cef_media_router_t, 80)
cefsizesok &= cefchecksize("cef_media_sink_device_info_callback_t", cef_media_sink_device_info_callback_t, 48)
cefsizesok &= cefchecksize("cef_media_sink_t", cef_media_sink_t, 104)
cefsizesok &= cefchecksize("cef_media_source_t", cef_media_source_t, 64)
cefsizesok &= cefchecksize("cef_menu_button_delegate_t", cef_menu_button_delegate_t, 144)
cefsizesok &= cefchecksize("cef_menu_button_pressed_lock_t", cef_menu_button_pressed_lock_t, 40)
cefsizesok &= cefchecksize("cef_menu_button_t", cef_menu_button_t, 592)
cefsizesok &= cefchecksize("cef_menu_model_delegate_t", cef_menu_model_delegate_t, 96)
cefsizesok &= cefchecksize("cef_menu_model_t", cef_menu_model_t, 488)
cefsizesok &= cefchecksize("cef_navigation_entry_t", cef_navigation_entry_t, 120)
cefsizesok &= cefchecksize("cef_navigation_entry_visitor_t", cef_navigation_entry_visitor_t, 48)
cefsizesok &= cefchecksize("cef_overlay_controller_t", cef_overlay_controller_t, 192)
cefsizesok &= cefchecksize("cef_panel_delegate_t", cef_panel_delegate_t, 120)
cefsizesok &= cefchecksize("cef_panel_t", cef_panel_t, 536)
cefsizesok &= cefchecksize("cef_pdf_print_callback_t", cef_pdf_print_callback_t, 48)
cefsizesok &= cefchecksize("cef_permission_handler_t", cef_permission_handler_t, 64)
cefsizesok &= cefchecksize("cef_permission_prompt_callback_t", cef_permission_prompt_callback_t, 48)
cefsizesok &= cefchecksize("cef_post_data_element_t", cef_post_data_element_t, 104)
cefsizesok &= cefchecksize("cef_post_data_t", cef_post_data_t, 96)
cefsizesok &= cefchecksize("cef_preference_manager_t", cef_preference_manager_t, 80)
cefsizesok &= cefchecksize("cef_preference_registrar_t", cef_preference_registrar_t, 24)
cefsizesok &= cefchecksize("cef_print_dialog_callback_t", cef_print_dialog_callback_t, 56)
cefsizesok &= cefchecksize("cef_print_handler_t", cef_print_handler_t, 88)
cefsizesok &= cefchecksize("cef_print_job_callback_t", cef_print_job_callback_t, 48)
cefsizesok &= cefchecksize("cef_print_settings_t", cef_print_settings_t, 216)
cefsizesok &= cefchecksize("cef_process_message_t", cef_process_message_t, 88)
cefsizesok &= cefchecksize("cef_read_handler_t", cef_read_handler_t, 80)
cefsizesok &= cefchecksize("cef_registration_t", cef_registration_t, 40)
cefsizesok &= cefchecksize("cef_render_handler_t", cef_render_handler_t, 176)
cefsizesok &= cefchecksize("cef_render_process_handler_t", cef_render_process_handler_t, 112)
cefsizesok &= cefchecksize("cef_request_context_handler_t", cef_request_context_handler_t, 56)
cefsizesok &= cefchecksize("cef_request_context_t", cef_request_context_t, 224)
cefsizesok &= cefchecksize("cef_request_handler_t", cef_request_handler_t, 112)
cefsizesok &= cefchecksize("cef_request_t", cef_request_t, 216)
cefsizesok &= cefchecksize("cef_resolve_callback_t", cef_resolve_callback_t, 48)
cefsizesok &= cefchecksize("cef_resource_bundle_handler_t", cef_resource_bundle_handler_t, 64)
cefsizesok &= cefchecksize("cef_resource_bundle_t", cef_resource_bundle_t, 64)
cefsizesok &= cefchecksize("cef_resource_handler_t", cef_resource_handler_t, 96)
cefsizesok &= cefchecksize("cef_resource_read_callback_t", cef_resource_read_callback_t, 48)
cefsizesok &= cefchecksize("cef_resource_request_handler_t", cef_resource_request_handler_t, 104)
cefsizesok &= cefchecksize("cef_resource_skip_callback_t", cef_resource_skip_callback_t, 48)
cefsizesok &= cefchecksize("cef_response_filter_t", cef_response_filter_t, 56)
cefsizesok &= cefchecksize("cef_response_t", cef_response_t, 176)
cefsizesok &= cefchecksize("cef_run_context_menu_callback_t", cef_run_context_menu_callback_t, 56)
cefsizesok &= cefchecksize("cef_run_file_dialog_callback_t", cef_run_file_dialog_callback_t, 48)
cefsizesok &= cefchecksize("cef_run_quick_menu_callback_t", cef_run_quick_menu_callback_t, 56)
cefsizesok &= cefchecksize("cef_scheme_handler_factory_t", cef_scheme_handler_factory_t, 48)
cefsizesok &= cefchecksize("cef_scheme_registrar_t", cef_scheme_registrar_t, 24)
cefsizesok &= cefchecksize("cef_scroll_view_t", cef_scroll_view_t, 496)
cefsizesok &= cefchecksize("cef_select_client_certificate_callback_t", cef_select_client_certificate_callback_t, 48)
cefsizesok &= cefchecksize("cef_server_handler_t", cef_server_handler_t, 104)
cefsizesok &= cefchecksize("cef_server_t", cef_server_t, 144)
cefsizesok &= cefchecksize("cef_set_cookie_callback_t", cef_set_cookie_callback_t, 48)
cefsizesok &= cefchecksize("cef_shared_memory_region_t", cef_shared_memory_region_t, 64)
cefsizesok &= cefchecksize("cef_shared_process_message_builder_t", cef_shared_process_message_builder_t, 72)
cefsizesok &= cefchecksize("cef_sslinfo_t", cef_sslinfo_t, 56)
cefsizesok &= cefchecksize("cef_sslstatus_t", cef_sslstatus_t, 80)
cefsizesok &= cefchecksize("cef_stream_reader_t", cef_stream_reader_t, 80)
cefsizesok &= cefchecksize("cef_stream_writer_t", cef_stream_writer_t, 80)
cefsizesok &= cefchecksize("cef_string_visitor_t", cef_string_visitor_t, 48)
cefsizesok &= cefchecksize("cef_task_runner_t", cef_task_runner_t, 80)
cefsizesok &= cefchecksize("cef_task_t", cef_task_t, 48)
cefsizesok &= cefchecksize("cef_textfield_delegate_t", cef_textfield_delegate_t, 136)
cefsizesok &= cefchecksize("cef_textfield_t", cef_textfield_t, 688)
cefsizesok &= cefchecksize("cef_thread_t", cef_thread_t, 72)
cefsizesok &= cefchecksize("cef_urlrequest_client_t", cef_urlrequest_client_t, 80)
cefsizesok &= cefchecksize("cef_urlrequest_t", cef_urlrequest_t, 96)
cefsizesok &= cefchecksize("cef_v8accessor_t", cef_v8accessor_t, 56)
cefsizesok &= cefchecksize("cef_v8array_buffer_release_callback_t", cef_v8array_buffer_release_callback_t, 48)
cefsizesok &= cefchecksize("cef_v8context_t", cef_v8context_t, 112)
cefsizesok &= cefchecksize("cef_v8exception_t", cef_v8exception_t, 104)
cefsizesok &= cefchecksize("cef_v8handler_t", cef_v8handler_t, 48)
cefsizesok &= cefchecksize("cef_v8interceptor_t", cef_v8interceptor_t, 72)
cefsizesok &= cefchecksize("cef_v8stack_frame_t", cef_v8stack_frame_t, 104)
cefsizesok &= cefchecksize("cef_v8stack_trace_t", cef_v8stack_trace_t, 64)
cefsizesok &= cefchecksize("cef_v8value_t", cef_v8value_t, 440)
cefsizesok &= cefchecksize("cef_value_t", cef_value_t, 216)
cefsizesok &= cefchecksize("cef_view_delegate_t", cef_view_delegate_t, 120)
cefsizesok &= cefchecksize("cef_view_t", cef_view_t, 440)
cefsizesok &= cefchecksize("cef_waitable_event_t", cef_waitable_event_t, 80)
cefsizesok &= cefchecksize("cef_window_delegate_t", cef_window_delegate_t, 240)
cefsizesok &= cefchecksize("cef_window_t", cef_window_t, 832)
cefsizesok &= cefchecksize("cef_write_handler_t", cef_write_handler_t, 80)
cefsizesok &= cefchecksize("cef_x509cert_principal_t", cef_x509cert_principal_t, 112)
cefsizesok &= cefchecksize("cef_x509certificate_t", cef_x509certificate_t, 120)
cefsizesok &= cefchecksize("cef_xml_reader_t", cef_xml_reader_t, 272)
cefsizesok &= cefchecksize("cef_zip_reader_t", cef_zip_reader_t, 136)
cefsizesok &= cefchecksize("cef_basetime_t", cef_basetime_t, 8)
cefsizesok &= cefchecksize("cef_time_t", cef_time_t, 32)
cefsizesok &= cefchecksize("cef_settings_t", cef_settings_t, 440)
cefsizesok &= cefchecksize("cef_request_context_settings_t", cef_request_context_settings_t, 96)
cefsizesok &= cefchecksize("cef_browser_settings_t", cef_browser_settings_t, 288)
cefsizesok &= cefchecksize("cef_urlparts_t", cef_urlparts_t, 240)
cefsizesok &= cefchecksize("cef_cookie_t", cef_cookie_t, 144)
cefsizesok &= cefchecksize("cef_draggable_region_t", cef_draggable_region_t, 20)
cefsizesok &= cefchecksize("cef_screen_info_t", cef_screen_info_t, 48)
cefsizesok &= cefchecksize("cef_mouse_event_t", cef_mouse_event_t, 12)
cefsizesok &= cefchecksize("cef_touch_event_t", cef_touch_event_t, 40)
cefsizesok &= cefchecksize("cef_key_event_t", cef_key_event_t, 28)
cefsizesok &= cefchecksize("cef_popup_features_t", cef_popup_features_t, 48)
cefsizesok &= cefchecksize("cef_cursor_info_t", cef_cursor_info_t, 32)
cefsizesok &= cefchecksize("cef_pdf_print_settings_t", cef_pdf_print_settings_t, 152)
cefsizesok &= cefchecksize("cef_box_layout_settings_t", cef_box_layout_settings_t, 48)
cefsizesok &= cefchecksize("cef_range_t", cef_range_t, 8)
cefsizesok &= cefchecksize("cef_composition_underline_t", cef_composition_underline_t, 24)
cefsizesok &= cefchecksize("cef_audio_parameters_t", cef_audio_parameters_t, 12)
cefsizesok &= cefchecksize("cef_media_sink_device_info_t", cef_media_sink_device_info_t, 56)
cefsizesok &= cefchecksize("cef_touch_handle_state_t", cef_touch_handle_state_t, 36)
cefsizesok &= cefchecksize("cef_point_t", cef_point_t, 8)
cefsizesok &= cefchecksize("cef_rect_t", cef_rect_t, 16)
cefsizesok &= cefchecksize("cef_size_t", cef_size_t, 8)
cefsizesok &= cefchecksize("cef_insets_t", cef_insets_t, 16)
cefsizesok &= cefchecksize("cef_main_args_t", cef_main_args_t, 8)
cefsizesok &= cefchecksize("cef_window_info_t", cef_window_info_t, 96)
assert cefsizesok == 1