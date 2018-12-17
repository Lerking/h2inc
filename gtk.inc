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
 
%ifndef __GTK_H__ 
$define __GTK_H__ 
$define __GTK_H_INSIDE__ 
$include "gdk/gdk.inc" 
$include "gtk/gtkaboutdialog.inc" 
$include "gtk/gtkaccelgroup.inc" 
$include "gtk/gtkaccellabel.inc" 
$include "gtk/gtkaccelmap.inc" 
$include "gtk/gtkaccessible.inc" 
$include "gtk/gtkactionable.inc" 
$include "gtk/gtkactionbar.inc" 
$include "gtk/gtkadjustment.inc" 
$include "gtk/gtkappchooser.inc" 
$include "gtk/gtkappchooserdialog.inc" 
$include "gtk/gtkappchooserwidget.inc" 
$include "gtk/gtkappchooserbutton.inc" 
$include "gtk/gtkapplication.inc" 
$include "gtk/gtkapplicationwindow.inc" 
$include "gtk/gtkaspectframe.inc" 
$include "gtk/gtkassistant.inc" 
$include "gtk/gtkbbox.inc" 
$include "gtk/gtkbin.inc" 
$include "gtk/gtkbindings.inc" 
$include "gtk/gtkborder.inc" 
$include "gtk/gtkbox.inc" 
$include "gtk/gtkbuildable.inc" 
$include "gtk/gtkbuilder.inc" 
$include "gtk/gtkbutton.inc" 
$include "gtk/gtkcalendar.inc" 
$include "gtk/gtkcellarea.inc" 
$include "gtk/gtkcellareabox.inc" 
$include "gtk/gtkcellareacontext.inc" 
$include "gtk/gtkcelleditable.inc" 
$include "gtk/gtkcelllayout.inc" 
$include "gtk/gtkcellrenderer.inc" 
$include "gtk/gtkcellrendereraccel.inc" 
$include "gtk/gtkcellrenderercombo.inc" 
$include "gtk/gtkcellrendererpixbuf.inc" 
$include "gtk/gtkcellrendererprogress.inc" 
$include "gtk/gtkcellrendererspin.inc" 
$include "gtk/gtkcellrendererspinner.inc" 
$include "gtk/gtkcellrenderertext.inc" 
$include "gtk/gtkcellrenderertoggle.inc" 
$include "gtk/gtkcellview.inc" 
$include "gtk/gtkcheckbutton.inc" 
$include "gtk/gtkcheckmenuitem.inc" 
$include "gtk/gtkclipboard.inc" 
$include "gtk/gtkcolorbutton.inc" 
$include "gtk/gtkcolorchooser.inc" 
$include "gtk/gtkcolorchooserdialog.inc" 
$include "gtk/gtkcolorchooserwidget.inc" 
$include "gtk/gtkcolorutils.inc" 
$include "gtk/gtkcombobox.inc" 
$include "gtk/gtkcomboboxtext.inc" 
$include "gtk/gtkcontainer.inc" 
$include "gtk/gtkcssprovider.inc" 
$include "gtk/gtkcsssection.inc" 
$include "gtk/gtkdebug.inc" 
$include "gtk/gtkdialog.inc" 
$include "gtk/gtkdnd.inc" 
$include "gtk/gtkdrawingarea.inc" 
$include "gtk/gtkeditable.inc" 
$include "gtk/gtkentry.inc" 
$include "gtk/gtkentrybuffer.inc" 
$include "gtk/gtkentrycompletion.inc" 
$include "gtk/gtkenums.inc" 
$include "gtk/gtkeventbox.inc" 
$include "gtk/gtkeventcontroller.inc" 
$include "gtk/gtkexpander.inc" 
$include "gtk/gtkfixed.inc" 
$include "gtk/gtkfilechooser.inc" 
$include "gtk/gtkfilechooserbutton.inc" 
$include "gtk/gtkfilechooserdialog.inc" 
$include "gtk/gtkfilechooserwidget.inc" 
$include "gtk/gtkfilefilter.inc" 
$include "gtk/gtkflowbox.inc" 
$include "gtk/gtkfontbutton.inc" 
$include "gtk/gtkfontchooser.inc" 
$include "gtk/gtkfontchooserdialog.inc" 
$include "gtk/gtkfontchooserwidget.inc" 
$include "gtk/gtkframe.inc" 
$include "gtk/gtkgesture.inc" 
$include "gtk/gtkgesturedrag.inc" 
$include "gtk/gtkgesturelongpress.inc" 
$include "gtk/gtkgesturemultipress.inc" 
$include "gtk/gtkgesturepan.inc" 
$include "gtk/gtkgesturerotate.inc" 
$include "gtk/gtkgesturesingle.inc" 
$include "gtk/gtkgestureswipe.inc" 
$include "gtk/gtkgesturezoom.inc" 
$include "gtk/gtkglarea.inc" 
$include "gtk/gtkgrid.inc" 
$include "gtk/gtkheaderbar.inc" 
$include "gtk/gtkicontheme.inc" 
$include "gtk/gtkiconview.inc" 
$include "gtk/gtkimage.inc" 
$include "gtk/gtkimcontext.inc" 
$include "gtk/gtkimcontextinfo.inc" 
$include "gtk/gtkimcontextsimple.inc" 
$include "gtk/gtkimmulticontext.inc" 
$include "gtk/gtkinfobar.inc" 
$include "gtk/gtkinvisible.inc" 
$include "gtk/gtklabel.inc" 
$include "gtk/gtklayout.inc" 
$include "gtk/gtklevelbar.inc" 
$include "gtk/gtklinkbutton.inc" 
$include "gtk/gtklistbox.inc" 
$include "gtk/gtkliststore.inc" 
$include "gtk/gtklockbutton.inc" 
$include "gtk/gtkmain.inc" 
$include "gtk/gtkmenu.inc" 
$include "gtk/gtkmenubar.inc" 
$include "gtk/gtkmenubutton.inc" 
$include "gtk/gtkmenuitem.inc" 
$include "gtk/gtkmenushell.inc" 
$include "gtk/gtkmenutoolbutton.inc" 
$include "gtk/gtkmessagedialog.inc" 
$include "gtk/gtkmodelbutton.inc" 
$include "gtk/gtkmodules.inc" 
$include "gtk/gtkmountoperation.inc" 
$include "gtk/gtknotebook.inc" 
$include "gtk/gtkoffscreenwindow.inc" 
$include "gtk/gtkorientable.inc" 
$include "gtk/gtkoverlay.inc" 
$include "gtk/gtkpagesetup.inc" 
$include "gtk/gtkpapersize.inc" 
$include "gtk/gtkpaned.inc" 
$include "gtk/gtkplacessidebar.inc" 
$include "gtk/gtkpopover.inc" 
$include "gtk/gtkpopovermenu.inc" 
$include "gtk/gtkprintcontext.inc" 
$include "gtk/gtkprintoperation.inc" 
$include "gtk/gtkprintoperationpreview.inc" 
$include "gtk/gtkprintsettings.inc" 
$include "gtk/gtkprogressbar.inc" 
$include "gtk/gtkradiobutton.inc" 
$include "gtk/gtkradiomenuitem.inc" 
$include "gtk/gtkradiotoolbutton.inc" 
$include "gtk/gtkrange.inc" 
$include "gtk/gtkrecentchooser.inc" 
$include "gtk/gtkrecentchooserdialog.inc" 
$include "gtk/gtkrecentchoosermenu.inc" 
$include "gtk/gtkrecentchooserwidget.inc" 
$include "gtk/gtkrecentfilter.inc" 
$include "gtk/gtkrecentmanager.inc" 
$include "gtk/gtkrender.inc" 
$include "gtk/gtkrevealer.inc" 
$include "gtk/gtkscale.inc" 
$include "gtk/gtkscalebutton.inc" 
$include "gtk/gtkscrollable.inc" 
$include "gtk/gtkscrollbar.inc" 
$include "gtk/gtkscrolledwindow.inc" 
$include "gtk/gtksearchbar.inc" 
$include "gtk/gtksearchentry.inc" 
$include "gtk/gtkselection.inc" 
$include "gtk/gtkseparator.inc" 
$include "gtk/gtkseparatormenuitem.inc" 
$include "gtk/gtkseparatortoolitem.inc" 
$include "gtk/gtksettings.inc" 
$include "gtk/gtkshow.inc" 
$include "gtk/gtkstacksidebar.inc" 
$include "gtk/gtksizegroup.inc" 
$include "gtk/gtksizerequest.inc" 
$include "gtk/gtkspinbutton.inc" 
$include "gtk/gtkspinner.inc" 
$include "gtk/gtkstack.inc" 
$include "gtk/gtkstackswitcher.inc" 
$include "gtk/gtkstatusbar.inc" 
$include "gtk/gtkstylecontext.inc" 
$include "gtk/gtkstyleprovider.inc" 
$include "gtk/gtkswitch.inc" 
$include "gtk/gtktextattributes.inc" 
$include "gtk/gtktextbuffer.inc" 
$include "gtk/gtktextbufferrichtext.inc" 
$include "gtk/gtktextchild.inc" 
$include "gtk/gtktextiter.inc" 
$include "gtk/gtktextmark.inc" 
$include "gtk/gtktexttag.inc" 
$include "gtk/gtktexttagtable.inc" 
$include "gtk/gtktextview.inc" 
$include "gtk/gtktogglebutton.inc" 
$include "gtk/gtktoggletoolbutton.inc" 
$include "gtk/gtktoolbar.inc" 
$include "gtk/gtktoolbutton.inc" 
$include "gtk/gtktoolitem.inc" 
$include "gtk/gtktoolitemgroup.inc" 
$include "gtk/gtktoolpalette.inc" 
$include "gtk/gtktoolshell.inc" 
$include "gtk/gtktooltip.inc" 
$include "gtk/gtktestutils.inc" 
$include "gtk/gtktreednd.inc" 
$include "gtk/gtktreemodel.inc" 
$include "gtk/gtktreemodelfilter.inc" 
$include "gtk/gtktreemodelsort.inc" 
$include "gtk/gtktreeselection.inc" 
$include "gtk/gtktreesortable.inc" 
$include "gtk/gtktreestore.inc" 
$include "gtk/gtktreeview.inc" 
$include "gtk/gtktreeviewcolumn.inc" 
$include "gtk/gtktypebuiltins.inc" 
$include "gtk/gtktypes.inc" 
$include "gtk/gtkversion.inc" 
$include "gtk/gtkviewport.inc" 
$include "gtk/gtkvolumebutton.inc" 
$include "gtk/gtkwidget.inc" 
$include "gtk/gtkwidgetpath.inc" 
$include "gtk/gtkwindow.inc" 
$include "gtk/gtkwindowgroup.inc" 
%ifndef GTK_DISABLE_DEPRECATED 
$include "gtk/deprecated/gtkarrow.inc" 
$include "gtk/deprecated/gtkactivatable.inc" 
$include "gtk/deprecated/gtkaction.inc" 
$include "gtk/deprecated/gtkactiongroup.inc" 
$include "gtk/deprecated/gtkalignment.inc" 
$include "gtk/deprecated/gtkcolorsel.inc" 
$include "gtk/deprecated/gtkcolorseldialog.inc" 
$include "gtk/deprecated/gtkfontsel.inc" 
$include "gtk/deprecated/gtkgradient.inc" 
$include "gtk/deprecated/gtkhandlebox.inc" 
$include "gtk/deprecated/gtkhbbox.inc" 
$include "gtk/deprecated/gtkhbox.inc" 
$include "gtk/deprecated/gtkhpaned.inc" 
$include "gtk/deprecated/gtkhsv.inc" 
$include "gtk/deprecated/gtkhscale.inc" 
$include "gtk/deprecated/gtkhscrollbar.inc" 
$include "gtk/deprecated/gtkhseparator.inc" 
$include "gtk/deprecated/gtkiconfactory.inc" 
$include "gtk/deprecated/gtkimagemenuitem.inc" 
$include "gtk/deprecated/gtkmisc.inc" 
$include "gtk/deprecated/gtknumerableicon.inc" 
$include "gtk/deprecated/gtkradioaction.inc" 
$include "gtk/deprecated/gtkrc.inc" 
$include "gtk/deprecated/gtkrecentaction.inc" 
$include "gtk/deprecated/gtkstatusicon.inc" 
$include "gtk/deprecated/gtkstock.inc" 
$include "gtk/deprecated/gtkstyle.inc" 
$include "gtk/deprecated/gtkstyleproperties.inc" 
$include "gtk/deprecated/gtksymboliccolor.inc" 
$include "gtk/deprecated/gtktable.inc" 
$include "gtk/deprecated/gtktearoffmenuitem.inc" 
$include "gtk/deprecated/gtkthemingengine.inc" 
$include "gtk/deprecated/gtktoggleaction.inc" 
$include "gtk/deprecated/gtkuimanager.inc" 
$include "gtk/deprecated/gtkvbbox.inc" 
$include "gtk/deprecated/gtkvbox.inc" 
$include "gtk/deprecated/gtkvpaned.inc" 
$include "gtk/deprecated/gtkvscale.inc" 
$include "gtk/deprecated/gtkvscrollbar.inc" 
$include "gtk/deprecated/gtkvseparator.inc" 
%endif ; GTK_DISABLE_DEPRECATED  
$include "gtk/gtk-autocleanups.inc" 
$undef __GTK_H_INSIDE__ 
%endif ; __GTK_H__  