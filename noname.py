# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec  8 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BingWx
###########################################################################

class BingWx ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"bing壁纸宝", pos = wx.DefaultPosition, size = wx.Size( 640,580 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 640,580 ), wx.Size( 640,580 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.img_bitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"D:\\MyDocuments\\wuyh35\\My Documents\\My Pictures\\bing\\AberystwythSeafront.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 640,360 ), 0 )
		bSizer3.Add( self.img_bitmap, 0, 0, 5 )
		
		self.description_staticText = wx.StaticText( self, wx.ID_ANY, u"^.^", wx.DefaultPosition, wx.Size( 610,30 ), wx.ALIGN_CENTRE|wx.ST_ELLIPSIZE_END )
		self.description_staticText.Wrap( 2 )
		self.description_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		bSizer3.Add( self.description_staticText, 0, wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.left_bpButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"img/left_arrow.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 40,40 ), wx.BU_AUTODRAW )
		bSizer5.Add( self.left_bpButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.right_bpButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"img/right_arrow.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 40,40 ), wx.BU_AUTODRAW )
		bSizer5.Add( self.right_bpButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,2 ), wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.confirm_button = wx.Button( self, wx.ID_ANY, u"设为壁纸", wx.DefaultPosition, wx.Size( 280,-1 ), wx.BU_EXACTFIT )
		self.confirm_button.SetDefault() 
		self.confirm_button.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.confirm_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.confirm_button.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer3.Add( self.confirm_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Reload", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu2, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.left_bpButton.Bind( wx.EVT_BUTTON, self.previous_wallpaper )
		self.right_bpButton.Bind( wx.EVT_BUTTON, self.next_wallpaper )
		self.confirm_button.Bind( wx.EVT_BUTTON, self.change_wallpaper )
		self.Bind( wx.EVT_MENU, self.open_from_local, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.reload, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.exit, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.about_message, id = self.m_menuItem3.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def previous_wallpaper( self, event ):
		event.Skip()
	
	def next_wallpaper( self, event ):
		event.Skip()
	
	def change_wallpaper( self, event ):
		event.Skip()
	
	def open_from_local( self, event ):
		event.Skip()
	
	def reload( self, event ):
		event.Skip()
	
	def exit( self, event ):
		event.Skip()
	
	def about_message( self, event ):
		event.Skip()
	

