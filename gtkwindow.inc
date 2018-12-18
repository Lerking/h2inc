; GTK - The GIMP Toolkit 
; Copyright (C) 1995-1997 Peter Mattis, Spencer Kimball and Josh MacDonald 
; 
; This library is free software; you can redistribute it and/or 
; modify it under the terms of the GNU Lesser General Public 
; License as published by the Free Software Foundation; either 
; version 2 of the License, or (at your option) any later version. 
; 
; This library is distributed in the hope that it will be useful, 
; but WITHOUT ANY WARRANTY; without even the implied warranty of 
; MERCHANTABILITY or FITNESS A PARTICULAR PURPOSE. See the GNU 
; Lesser General Public License for more details. 
; 
; You should have received a copy of the GNU Lesser General Public 
; License along with this library. If not, see <http://www.gnu.org/licenses/>. 
 
; 
; Modified by the GTK+ Team and others 1997-2000. See the AUTHORS 
; file for a list of people on the GTK+ Team. See the ChangeLog 
; files for a list of changes. These files are distributed with 
; GTK+ at ftp://ftp.gtk.org/pub/gtk/. 
 
%ifndef __GTK_WINDOW_H__ 
%define __GTK_WINDOW_H__ 
%if !defined (__GTK_H_INSIDE__) && !defined (GTK_COMPILATION) 
%error "Only "gtk/gtk.inc" can be included directly." 
%endif 
%include "gtk/gtkapplication.inc" 
%include "gtk/gtkaccelgroup.inc" 
%include "gtk/gtkbin.inc" 
%define GTK_TYPE_WINDOW (gtk_window_get_type ()) 
%define GTK_WINDOW(obj) (G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_WINDOW, GtkWindow)) 
%define GTK_WINDOW_CLASS(klass) (G_TYPE_CHECK_CLASS_CAST ((klass), GTK_TYPE_WINDOW, GtkWindowClass)) 
%define GTK_IS_WINDOW(obj) (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_WINDOW)) 
%define GTK_IS_WINDOW_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GTK_TYPE_WINDOW)) 
%define GTK_WINDOW_GET_CLASS(obj) (G_TYPE_INSTANCE_GET_CLASS ((obj), GTK_TYPE_WINDOW, GtkWindowClass)) 
;  typedef struct _GtkWindowPrivate GtkWindowPrivate; 
;  typedef struct _GtkWindowClass GtkWindowClass; 
;  typedef struct _GtkWindowGeometryInfo GtkWindowGeometryInfo; 
;  typedef struct _GtkWindowGroup GtkWindowGroup; 
;  typedef struct _GtkWindowGroupClass GtkWindowGroupClass; 
;  typedef struct _GtkWindowGroupPrivate GtkWindowGroupPrivate; 
; GtkWindowClass: 
; @parent_class: The parent class. 
; @set_focus: Sets child as the focus widget for the window. 
; @activate_focus: Activates the current focused widget within the window. 
; @activate_default: Activates the default widget for the window. 
; @keys_changed: Signal gets emitted when the set of accelerators or 
; mnemonics that are associated with window changes. 
; @enable_debugging: Class handler for the #GtkWindow::enable-debugging 
; keybinding signal. Since: 3.14 
 
; G_SIGNAL_ACTION signals for keybindings  
; Padding for future expansion  
; GtkWindowType: 
; @GTK_WINDOW_TOPLEVEL: A regular window, such as a dialog. 
; @GTK_WINDOW_POPUP: A special window such as a tooltip. 
; 
; A #GtkWindow can be one of these types. Most things you’d consider a 
; “window” should have type #GTK_WINDOW_TOPLEVEL; windows with this type 
; are managed by the window manager and have a frame by default (call 
; gtk_window_set_decorated() to toggle the frame). Windows with type 
; #GTK_WINDOW_POPUP are ignored by the window manager; window manager 
; keybindings won’t work on them, the window manager won’t decorate the 
; window with a frame, many GTK+ features that rely on the window 
; manager will not work (e.g. resize grips and 
; maximization/minimization). #GTK_WINDOW_POPUP is used to implement 
; widgets such as #GtkMenu or tooltips that you normally don’t think of 
; as windows per se. Nearly all windows should be #GTK_WINDOW_TOPLEVEL. 
; In particular, do not use #GTK_WINDOW_POPUP just to turn off 
; the window borders; use gtk_window_set_decorated() for that. 
 
GTK_WINDOW_TOPLEVEL	 EQU	 0
 
GTK_WINDOW_POPUP	 EQU	 1
 
/**	 EQU	 2
 
; GtkWindowPosition: 
; @GTK_WIN_POS_NONE: No influence is made on placement. 
; @GTK_WIN_POS_CENTER: Windows should be placed in the center of the screen. 
; @GTK_WIN_POS_MOUSE: Windows should be placed at the current mouse position. 
; @GTK_WIN_POS_CENTER_ALWAYS: Keep window centered as it changes size, etc. 
; @GTK_WIN_POS_CENTER_ON_PARENT: Center the window on its transient 
; parent (see gtk_window_set_transient_for()). 
; 
; Window placement can be influenced using this enumeration. Note that 
; using #GTK_WIN_POS_CENTER_ALWAYS is almost always a bad idea. 
; It won’t necessarily work well with all window managers or on all windowing systems. 
 
GTK_WIN_POS_NONE	 EQU	 3
 
GTK_WIN_POS_CENTER	 EQU	 4
 
GTK_WIN_POS_MOUSE	 EQU	 5
 
GTK_WIN_POS_CENTER_ALWAYS	 EQU	 6
 
GTK_WIN_POS_CENTER_ON_PARENT	 EQU	 7
 
GDK_AVAILABLE_IN_ALL	 EQU	 8
 
GDK_AVAILABLE_IN_ALL	 EQU	 9
 
GDK_AVAILABLE_IN_ALL	 EQU	 10
 
GDK_AVAILABLE_IN_ALL	 EQU	 11
 
GDK_AVAILABLE_IN_ALL	 EQU	 12
 
GDK_AVAILABLE_IN_ALL	 EQU	 13
 
GDK_AVAILABLE_IN_ALL	 EQU	 14
 
GDK_AVAILABLE_IN_ALL	 EQU	 15
 
GDK_AVAILABLE_IN_ALL	 EQU	 16
 
GDK_AVAILABLE_IN_ALL	 EQU	 17
 
GDK_AVAILABLE_IN_ALL	 EQU	 18
 
GDK_AVAILABLE_IN_ALL	 EQU	 19
 
GDK_AVAILABLE_IN_ALL	 EQU	 20
 
GDK_AVAILABLE_IN_ALL	 EQU	 21
 
GDK_AVAILABLE_IN_ALL	 EQU	 22
 
GDK_AVAILABLE_IN_ALL	 EQU	 23
 
GDK_AVAILABLE_IN_ALL	 EQU	 24
 
GDK_AVAILABLE_IN_ALL	 EQU	 25
 
GDK_AVAILABLE_IN_ALL	 EQU	 26
 
GDK_AVAILABLE_IN_3_4	 EQU	 27
 
GDK_AVAILABLE_IN_3_4	 EQU	 28
 
GDK_DEPRECATED_IN_3_8_FOR(gtk_widget_set_opacity)	 EQU	 29
 
GDK_DEPRECATED_IN_3_8_FOR(gtk_widget_get_opacity)	 EQU	 30
 
GDK_AVAILABLE_IN_ALL	 EQU	 31
 
GDK_AVAILABLE_IN_ALL	 EQU	 32
 
GDK_AVAILABLE_IN_ALL	 EQU	 33
 
GDK_AVAILABLE_IN_ALL	 EQU	 34
 
GDK_AVAILABLE_IN_ALL	 EQU	 35
 
GDK_AVAILABLE_IN_ALL	 EQU	 36
 
GDK_AVAILABLE_IN_ALL	 EQU	 37
 
GDK_AVAILABLE_IN_ALL	 EQU	 38
 
GDK_AVAILABLE_IN_ALL	 EQU	 39
 
GDK_AVAILABLE_IN_ALL	 EQU	 40
 
GDK_AVAILABLE_IN_ALL	 EQU	 41
 
GDK_AVAILABLE_IN_ALL	 EQU	 42
 
GDK_AVAILABLE_IN_ALL	 EQU	 43
 
GDK_AVAILABLE_IN_ALL	 EQU	 44
 
GDK_AVAILABLE_IN_3_4	 EQU	 45
 
GDK_AVAILABLE_IN_3_4	 EQU	 46
 
GDK_AVAILABLE_IN_ALL	 EQU	 47
 
GDK_AVAILABLE_IN_ALL	 EQU	 48
 
GDK_AVAILABLE_IN_3_2	 EQU	 49
 
GDK_AVAILABLE_IN_3_2	 EQU	 50
 
GDK_AVAILABLE_IN_ALL	 EQU	 51
 
GDK_AVAILABLE_IN_ALL	 EQU	 52
 
GDK_AVAILABLE_IN_ALL	 EQU	 53
 
GDK_AVAILABLE_IN_ALL	 EQU	 54
 
GDK_AVAILABLE_IN_ALL	 EQU	 55
 
GDK_AVAILABLE_IN_ALL	 EQU	 56
 
GDK_AVAILABLE_IN_ALL	 EQU	 57
 
GDK_AVAILABLE_IN_ALL	 EQU	 58
 
GDK_AVAILABLE_IN_ALL	 EQU	 59
 
GDK_AVAILABLE_IN_ALL	 EQU	 60
 
GDK_AVAILABLE_IN_ALL	 EQU	 61
 
GDK_AVAILABLE_IN_ALL	 EQU	 62
 
GDK_AVAILABLE_IN_ALL	 EQU	 63
 
GDK_AVAILABLE_IN_ALL	 EQU	 64
 
GDK_AVAILABLE_IN_ALL	 EQU	 65
 
GDK_AVAILABLE_IN_ALL	 EQU	 66
 
GDK_AVAILABLE_IN_ALL	 EQU	 67
 
GDK_AVAILABLE_IN_ALL	 EQU	 68
 
GDK_AVAILABLE_IN_ALL	 EQU	 69
 
GDK_AVAILABLE_IN_ALL	 EQU	 70
 
GDK_AVAILABLE_IN_ALL	 EQU	 71
 
GDK_AVAILABLE_IN_ALL	 EQU	 72
 
GDK_AVAILABLE_IN_ALL	 EQU	 73
 
GDK_AVAILABLE_IN_ALL	 EQU	 74
 
GDK_AVAILABLE_IN_ALL	 EQU	 75
 
GDK_AVAILABLE_IN_ALL	 EQU	 76
 
GDK_AVAILABLE_IN_ALL	 EQU	 77
 
; If window is set modal, input will be grabbed when show and released when hide  
GDK_AVAILABLE_IN_ALL	 EQU	 78
 
GDK_AVAILABLE_IN_ALL	 EQU	 79
 
GDK_AVAILABLE_IN_ALL	 EQU	 80
 
GDK_AVAILABLE_IN_ALL	 EQU	 81
 
GDK_AVAILABLE_IN_ALL	 EQU	 82
 
GDK_AVAILABLE_IN_ALL	 EQU	 83
 
GDK_AVAILABLE_IN_ALL	 EQU	 84
 
GDK_AVAILABLE_IN_ALL	 EQU	 85
 
GDK_AVAILABLE_IN_ALL	 EQU	 86
 
GDK_AVAILABLE_IN_ALL	 EQU	 87
 
GDK_AVAILABLE_IN_ALL	 EQU	 88
 
GDK_AVAILABLE_IN_ALL	 EQU	 89
 
GDK_AVAILABLE_IN_ALL	 EQU	 90
 
GDK_AVAILABLE_IN_ALL	 EQU	 91
 
GDK_AVAILABLE_IN_ALL	 EQU	 92
 
GDK_AVAILABLE_IN_ALL	 EQU	 93
 
GDK_AVAILABLE_IN_ALL	 EQU	 94
 
GDK_AVAILABLE_IN_ALL	 EQU	 95
 
GDK_AVAILABLE_IN_ALL	 EQU	 96
 
GDK_AVAILABLE_IN_ALL	 EQU	 97
 
GDK_AVAILABLE_IN_ALL	 EQU	 98
 
GDK_AVAILABLE_IN_3_18	 EQU	 99
 
GDK_AVAILABLE_IN_3_10	 EQU	 100
 
GDK_AVAILABLE_IN_ALL	 EQU	 101
 
GDK_AVAILABLE_IN_ALL	 EQU	 102
 
GDK_AVAILABLE_IN_ALL	 EQU	 103
 
GDK_AVAILABLE_IN_ALL	 EQU	 104
 
; Set initial default size of the window (does not constrain user 
; resize operations) 
 
GDK_AVAILABLE_IN_ALL	 EQU	 105
 
GDK_AVAILABLE_IN_ALL	 EQU	 106
 
GDK_AVAILABLE_IN_ALL	 EQU	 107
 
GDK_AVAILABLE_IN_ALL	 EQU	 108
 
GDK_AVAILABLE_IN_ALL	 EQU	 109
 
GDK_AVAILABLE_IN_ALL	 EQU	 110
 
GDK_AVAILABLE_IN_ALL	 EQU	 111
 
GDK_AVAILABLE_IN_ALL	 EQU	 112
 
GDK_AVAILABLE_IN_ALL	 EQU	 113
 
GDK_AVAILABLE_IN_ALL	 EQU	 114
 
GDK_AVAILABLE_IN_ALL	 EQU	 115
 
; Ignore this unless you are writing a GUI builder  
GDK_DEPRECATED_IN_3_10	 EQU	 116
 
GDK_AVAILABLE_IN_ALL	 EQU	 117
 
GDK_AVAILABLE_IN_ALL	 EQU	 118
 
GDK_AVAILABLE_IN_ALL	 EQU	 119
 
; Window grips 
 
GDK_DEPRECATED_IN_3_14	 EQU	 120
 
GDK_DEPRECATED_IN_3_14	 EQU	 121
 
GDK_DEPRECATED_IN_3_14	 EQU	 122
 
GDK_DEPRECATED_IN_3_14	 EQU	 123
 
GDK_AVAILABLE_IN_3_10	 EQU	 124
 
GDK_AVAILABLE_IN_3_16	 EQU	 125
 
GDK_AVAILABLE_IN_3_12	 EQU	 126
 
GDK_AVAILABLE_IN_3_14	 EQU	 127
 
G_END_DECLS	 EQU	 128
 
%endif ; __GTK_WINDOW_H__  
