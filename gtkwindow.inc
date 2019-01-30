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
 
struc GtkWindowPrivate 
endstruc 
struc GtkWindowClass 
endstruc 
struc GtkWindowGeometryInfo 
endstruc 
struc GtkWindowGroup 
endstruc 
struc GtkWindowGroupClass 
endstruc 
struc GtkWindowGroupPrivate 
endstruc 
 
 
 
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
 
GTK_WIN_POS_NONE	 EQU	 0 
GTK_WIN_POS_CENTER	 EQU	 1 
GTK_WIN_POS_MOUSE	 EQU	 2 
GTK_WIN_POS_CENTER_ALWAYS	 EQU	 3 
GTK_WIN_POS_CENTER_ON_PARENT	 EQU	 4 
 
 
const gchar ; gtk_window_get_title (GtkWindow *window); 
const gchar ; gtk_window_get_role (GtkWindow *window); 
 
 
 
 
 
 
 
 
 
const gchar ; gtk_window_get_icon_name (GtkWindow *window); 
const gchar ; gtk_window_get_default_icon_name (void); 
 
 
; If window is set modal, input will be grabbed when show and released when hide  
 
 
 
 
 
; Set initial default size of the window (does not constrain user 
; resize operations) 
 
 
 
 
; Ignore this unless you are writing a GUI builder  
 
 
 
 
 
; Window grips 
 
 
 
 
 
 
#endif ; __GTK_WINDOW_H__  
