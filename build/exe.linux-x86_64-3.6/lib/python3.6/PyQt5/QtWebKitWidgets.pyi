# The PEP 484 type hints stub file for the QtWebKitWidgets module.
#
# Generated by SIP 4.19.6
#
# Copyright (c) 2017 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWidgets
from PyQt5 import QtWebKit
from PyQt5 import QtPrintSupport
from PyQt5 import QtNetwork
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QGraphicsWebView(QtWidgets.QGraphicsWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QGraphicsItem] = ...) -> None: ...

    def setRenderHint(self, hint: QtGui.QPainter.RenderHint, enabled: bool = ...) -> None: ...
    def setRenderHints(self, hints: QtGui.QPainter.RenderHints) -> None: ...
    def renderHints(self) -> QtGui.QPainter.RenderHints: ...
    def setTiledBackingStoreFrozen(self, frozen: bool) -> None: ...
    def isTiledBackingStoreFrozen(self) -> bool: ...
    def setResizesToContents(self, enabled: bool) -> None: ...
    def resizesToContents(self) -> bool: ...
    def sceneEvent(self, a0: QtCore.QEvent) -> bool: ...
    def focusNextPrevChild(self, next: bool) -> bool: ...
    def inputMethodEvent(self, a0: QtGui.QInputMethodEvent) -> None: ...
    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None: ...
    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None: ...
    def dropEvent(self, a0: QtWidgets.QGraphicsSceneDragDropEvent) -> None: ...
    def dragMoveEvent(self, a0: QtWidgets.QGraphicsSceneDragDropEvent) -> None: ...
    def dragLeaveEvent(self, a0: QtWidgets.QGraphicsSceneDragDropEvent) -> None: ...
    def dragEnterEvent(self, a0: QtWidgets.QGraphicsSceneDragDropEvent) -> None: ...
    def contextMenuEvent(self, a0: QtWidgets.QGraphicsSceneContextMenuEvent) -> None: ...
    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None: ...
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None: ...
    def wheelEvent(self, a0: QtWidgets.QGraphicsSceneWheelEvent) -> None: ...
    def hoverLeaveEvent(self, a0: QtWidgets.QGraphicsSceneHoverEvent) -> None: ...
    def hoverMoveEvent(self, a0: QtWidgets.QGraphicsSceneHoverEvent) -> None: ...
    def mouseMoveEvent(self, a0: QtWidgets.QGraphicsSceneMouseEvent) -> None: ...
    def mouseReleaseEvent(self, a0: QtWidgets.QGraphicsSceneMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, a0: QtWidgets.QGraphicsSceneMouseEvent) -> None: ...
    def mousePressEvent(self, a0: QtWidgets.QGraphicsSceneMouseEvent) -> None: ...
    def linkClicked(self, a0: QtCore.QUrl) -> None: ...
    def statusBarMessage(self, message: str) -> None: ...
    def iconChanged(self) -> None: ...
    def titleChanged(self, a0: str) -> None: ...
    def urlChanged(self, a0: QtCore.QUrl) -> None: ...
    def loadProgress(self, progress: int) -> None: ...
    def loadFinished(self, a0: bool) -> None: ...
    def loadStarted(self) -> None: ...
    def reload(self) -> None: ...
    def forward(self) -> None: ...
    def back(self) -> None: ...
    def stop(self) -> None: ...
    def inputMethodQuery(self, query: QtCore.Qt.InputMethodQuery) -> typing.Any: ...
    def sizeHint(self, which: QtCore.Qt.SizeHint, constraint: QtCore.QSizeF) -> QtCore.QSizeF: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def itemChange(self, change: QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any: ...
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def updateGeometry(self) -> None: ...
    def setGeometry(self, rect: QtCore.QRectF) -> None: ...
    def findText(self, subString: str, options: 'QWebPage.FindFlags' = ...) -> bool: ...
    def triggerPageAction(self, action: 'QWebPage.WebAction', checked: bool = ...) -> None: ...
    def pageAction(self, action: 'QWebPage.WebAction') -> QtWidgets.QAction: ...
    def settings(self) -> QtWebKit.QWebSettings: ...
    def history(self) -> QtWebKit.QWebHistory: ...
    def setContent(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], mimeType: str = ..., baseUrl: QtCore.QUrl = ...) -> None: ...
    def setHtml(self, html: str, baseUrl: QtCore.QUrl = ...) -> None: ...
    @typing.overload
    def load(self, url: QtCore.QUrl) -> None: ...
    @typing.overload
    def load(self, request: QtNetwork.QNetworkRequest, operation: QtNetwork.QNetworkAccessManager.Operation = ..., body: typing.Union[QtCore.QByteArray, bytes, bytearray] = ...) -> None: ...
    def isModified(self) -> bool: ...
    def setZoomFactor(self, a0: float) -> None: ...
    def zoomFactor(self) -> float: ...
    def icon(self) -> QtGui.QIcon: ...
    def title(self) -> str: ...
    def setUrl(self, a0: QtCore.QUrl) -> None: ...
    def url(self) -> QtCore.QUrl: ...
    def setPage(self, a0: 'QWebPage') -> None: ...
    def page(self) -> 'QWebPage': ...


class QWebHitTestResult(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QWebHitTestResult') -> None: ...

    def linkTitleString(self) -> str: ...
    def mediaUrl(self) -> QtCore.QUrl: ...
    def element(self) -> QtWebKit.QWebElement: ...
    def linkElement(self) -> QtWebKit.QWebElement: ...
    def enclosingBlockElement(self) -> QtWebKit.QWebElement: ...
    def boundingRect(self) -> QtCore.QRect: ...
    def frame(self) -> 'QWebFrame': ...
    def isContentSelected(self) -> bool: ...
    def isContentEditable(self) -> bool: ...
    def pixmap(self) -> QtGui.QPixmap: ...
    def imageUrl(self) -> QtCore.QUrl: ...
    def alternateText(self) -> str: ...
    def linkTargetFrame(self) -> 'QWebFrame': ...
    def linkTitle(self) -> QtCore.QUrl: ...
    def linkUrl(self) -> QtCore.QUrl: ...
    def linkText(self) -> str: ...
    def title(self) -> str: ...
    def pos(self) -> QtCore.QPoint: ...
    def isNull(self) -> bool: ...


class QWebFrame(QtCore.QObject):

    class RenderLayer(int): ...
    ContentsLayer = ... # type: 'QWebFrame.RenderLayer'
    ScrollBarLayer = ... # type: 'QWebFrame.RenderLayer'
    PanIconLayer = ... # type: 'QWebFrame.RenderLayer'
    AllLayers = ... # type: 'QWebFrame.RenderLayer'

    class ValueOwnership(int): ...
    QtOwnership = ... # type: 'QWebFrame.ValueOwnership'
    ScriptOwnership = ... # type: 'QWebFrame.ValueOwnership'
    AutoOwnership = ... # type: 'QWebFrame.ValueOwnership'

    class RenderLayers(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QWebFrame.RenderLayers', 'QWebFrame.RenderLayer']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebFrame.RenderLayers') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QWebFrame.RenderLayers': ...
        def __int__(self) -> int: ...

    def scrollToAnchor(self, anchor: str) -> None: ...
    def pageChanged(self) -> None: ...
    def loadFinished(self, ok: bool) -> None: ...
    def loadStarted(self) -> None: ...
    def contentsSizeChanged(self, size: QtCore.QSize) -> None: ...
    def findFirstElement(self, selectorQuery: str) -> QtWebKit.QWebElement: ...
    def findAllElements(self, selectorQuery: str) -> QtWebKit.QWebElementCollection: ...
    def documentElement(self) -> QtWebKit.QWebElement: ...
    def setFocus(self) -> None: ...
    def hasFocus(self) -> bool: ...
    @typing.overload
    def render(self, a0: QtGui.QPainter, clip: QtGui.QRegion = ...) -> None: ...
    @typing.overload
    def render(self, a0: QtGui.QPainter, layer: 'QWebFrame.RenderLayers', clip: QtGui.QRegion = ...) -> None: ...
    def scrollBarGeometry(self, orientation: QtCore.Qt.Orientation) -> QtCore.QRect: ...
    def baseUrl(self) -> QtCore.QUrl: ...
    def requestedUrl(self) -> QtCore.QUrl: ...
    def securityOrigin(self) -> QtWebKit.QWebSecurityOrigin: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def zoomFactor(self) -> float: ...
    def setScrollPosition(self, pos: QtCore.QPoint) -> None: ...
    def scrollPosition(self) -> QtCore.QPoint: ...
    def scroll(self, a0: int, a1: int) -> None: ...
    def metaData(self) -> typing.Any: ...
    def iconChanged(self) -> None: ...
    def initialLayoutCompleted(self) -> None: ...
    def urlChanged(self, url: QtCore.QUrl) -> None: ...
    def titleChanged(self, title: str) -> None: ...
    def javaScriptWindowObjectCleared(self) -> None: ...
    def print(self, printer: QtPrintSupport.QPrinter) -> None: ...
    def print_(self, printer: QtPrintSupport.QPrinter) -> None: ...
    def evaluateJavaScript(self, scriptSource: str) -> typing.Any: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def hitTestContent(self, pos: QtCore.QPoint) -> QWebHitTestResult: ...
    def contentsSize(self) -> QtCore.QSize: ...
    def geometry(self) -> QtCore.QRect: ...
    def pos(self) -> QtCore.QPoint: ...
    def scrollBarMaximum(self, orientation: QtCore.Qt.Orientation) -> int: ...
    def scrollBarMinimum(self, orientation: QtCore.Qt.Orientation) -> int: ...
    def scrollBarValue(self, orientation: QtCore.Qt.Orientation) -> int: ...
    def setScrollBarValue(self, orientation: QtCore.Qt.Orientation, value: int) -> None: ...
    def setScrollBarPolicy(self, orientation: QtCore.Qt.Orientation, policy: QtCore.Qt.ScrollBarPolicy) -> None: ...
    def scrollBarPolicy(self, orientation: QtCore.Qt.Orientation) -> QtCore.Qt.ScrollBarPolicy: ...
    def childFrames(self) -> typing.Any: ...
    def parentFrame(self) -> 'QWebFrame': ...
    def frameName(self) -> str: ...
    def icon(self) -> QtGui.QIcon: ...
    def url(self) -> QtCore.QUrl: ...
    def setUrl(self, url: QtCore.QUrl) -> None: ...
    def title(self) -> str: ...
    def toPlainText(self) -> str: ...
    def toHtml(self) -> str: ...
    def addToJavaScriptWindowObject(self, name: str, object: QtCore.QObject, ownership: 'QWebFrame.ValueOwnership' = ...) -> None: ...
    def setContent(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], mimeType: str = ..., baseUrl: QtCore.QUrl = ...) -> None: ...
    def setHtml(self, html: str, baseUrl: QtCore.QUrl = ...) -> None: ...
    @typing.overload
    def load(self, url: QtCore.QUrl) -> None: ...
    @typing.overload
    def load(self, request: QtNetwork.QNetworkRequest, operation: QtNetwork.QNetworkAccessManager.Operation = ..., body: typing.Union[QtCore.QByteArray, bytes, bytearray] = ...) -> None: ...
    def page(self) -> 'QWebPage': ...


class QWebInspector(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def hideEvent(self, event: QtGui.QHideEvent) -> None: ...
    def showEvent(self, event: QtGui.QShowEvent) -> None: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def page(self) -> 'QWebPage': ...
    def setPage(self, page: 'QWebPage') -> None: ...


class QWebPage(QtCore.QObject):

    class VisibilityState(int): ...
    VisibilityStateVisible = ... # type: 'QWebPage.VisibilityState'
    VisibilityStateHidden = ... # type: 'QWebPage.VisibilityState'
    VisibilityStatePrerender = ... # type: 'QWebPage.VisibilityState'
    VisibilityStateUnloaded = ... # type: 'QWebPage.VisibilityState'

    class Feature(int): ...
    Notifications = ... # type: 'QWebPage.Feature'
    Geolocation = ... # type: 'QWebPage.Feature'

    class PermissionPolicy(int): ...
    PermissionUnknown = ... # type: 'QWebPage.PermissionPolicy'
    PermissionGrantedByUser = ... # type: 'QWebPage.PermissionPolicy'
    PermissionDeniedByUser = ... # type: 'QWebPage.PermissionPolicy'

    class ErrorDomain(int): ...
    QtNetwork = ... # type: 'QWebPage.ErrorDomain'
    Http = ... # type: 'QWebPage.ErrorDomain'
    WebKit = ... # type: 'QWebPage.ErrorDomain'

    class Extension(int): ...
    ChooseMultipleFilesExtension = ... # type: 'QWebPage.Extension'
    ErrorPageExtension = ... # type: 'QWebPage.Extension'

    class WebWindowType(int): ...
    WebBrowserWindow = ... # type: 'QWebPage.WebWindowType'
    WebModalDialog = ... # type: 'QWebPage.WebWindowType'

    class LinkDelegationPolicy(int): ...
    DontDelegateLinks = ... # type: 'QWebPage.LinkDelegationPolicy'
    DelegateExternalLinks = ... # type: 'QWebPage.LinkDelegationPolicy'
    DelegateAllLinks = ... # type: 'QWebPage.LinkDelegationPolicy'

    class FindFlag(int): ...
    FindBackward = ... # type: 'QWebPage.FindFlag'
    FindCaseSensitively = ... # type: 'QWebPage.FindFlag'
    FindWrapsAroundDocument = ... # type: 'QWebPage.FindFlag'
    HighlightAllOccurrences = ... # type: 'QWebPage.FindFlag'
    FindAtWordBeginningsOnly = ... # type: 'QWebPage.FindFlag'
    TreatMedialCapitalAsWordBeginning = ... # type: 'QWebPage.FindFlag'
    FindBeginsInSelection = ... # type: 'QWebPage.FindFlag'

    class WebAction(int): ...
    NoWebAction = ... # type: 'QWebPage.WebAction'
    OpenLink = ... # type: 'QWebPage.WebAction'
    OpenLinkInNewWindow = ... # type: 'QWebPage.WebAction'
    OpenFrameInNewWindow = ... # type: 'QWebPage.WebAction'
    DownloadLinkToDisk = ... # type: 'QWebPage.WebAction'
    CopyLinkToClipboard = ... # type: 'QWebPage.WebAction'
    OpenImageInNewWindow = ... # type: 'QWebPage.WebAction'
    DownloadImageToDisk = ... # type: 'QWebPage.WebAction'
    CopyImageToClipboard = ... # type: 'QWebPage.WebAction'
    Back = ... # type: 'QWebPage.WebAction'
    Forward = ... # type: 'QWebPage.WebAction'
    Stop = ... # type: 'QWebPage.WebAction'
    Reload = ... # type: 'QWebPage.WebAction'
    Cut = ... # type: 'QWebPage.WebAction'
    Copy = ... # type: 'QWebPage.WebAction'
    Paste = ... # type: 'QWebPage.WebAction'
    Undo = ... # type: 'QWebPage.WebAction'
    Redo = ... # type: 'QWebPage.WebAction'
    MoveToNextChar = ... # type: 'QWebPage.WebAction'
    MoveToPreviousChar = ... # type: 'QWebPage.WebAction'
    MoveToNextWord = ... # type: 'QWebPage.WebAction'
    MoveToPreviousWord = ... # type: 'QWebPage.WebAction'
    MoveToNextLine = ... # type: 'QWebPage.WebAction'
    MoveToPreviousLine = ... # type: 'QWebPage.WebAction'
    MoveToStartOfLine = ... # type: 'QWebPage.WebAction'
    MoveToEndOfLine = ... # type: 'QWebPage.WebAction'
    MoveToStartOfBlock = ... # type: 'QWebPage.WebAction'
    MoveToEndOfBlock = ... # type: 'QWebPage.WebAction'
    MoveToStartOfDocument = ... # type: 'QWebPage.WebAction'
    MoveToEndOfDocument = ... # type: 'QWebPage.WebAction'
    SelectNextChar = ... # type: 'QWebPage.WebAction'
    SelectPreviousChar = ... # type: 'QWebPage.WebAction'
    SelectNextWord = ... # type: 'QWebPage.WebAction'
    SelectPreviousWord = ... # type: 'QWebPage.WebAction'
    SelectNextLine = ... # type: 'QWebPage.WebAction'
    SelectPreviousLine = ... # type: 'QWebPage.WebAction'
    SelectStartOfLine = ... # type: 'QWebPage.WebAction'
    SelectEndOfLine = ... # type: 'QWebPage.WebAction'
    SelectStartOfBlock = ... # type: 'QWebPage.WebAction'
    SelectEndOfBlock = ... # type: 'QWebPage.WebAction'
    SelectStartOfDocument = ... # type: 'QWebPage.WebAction'
    SelectEndOfDocument = ... # type: 'QWebPage.WebAction'
    DeleteStartOfWord = ... # type: 'QWebPage.WebAction'
    DeleteEndOfWord = ... # type: 'QWebPage.WebAction'
    SetTextDirectionDefault = ... # type: 'QWebPage.WebAction'
    SetTextDirectionLeftToRight = ... # type: 'QWebPage.WebAction'
    SetTextDirectionRightToLeft = ... # type: 'QWebPage.WebAction'
    ToggleBold = ... # type: 'QWebPage.WebAction'
    ToggleItalic = ... # type: 'QWebPage.WebAction'
    ToggleUnderline = ... # type: 'QWebPage.WebAction'
    InspectElement = ... # type: 'QWebPage.WebAction'
    InsertParagraphSeparator = ... # type: 'QWebPage.WebAction'
    InsertLineSeparator = ... # type: 'QWebPage.WebAction'
    SelectAll = ... # type: 'QWebPage.WebAction'
    ReloadAndBypassCache = ... # type: 'QWebPage.WebAction'
    PasteAndMatchStyle = ... # type: 'QWebPage.WebAction'
    RemoveFormat = ... # type: 'QWebPage.WebAction'
    ToggleStrikethrough = ... # type: 'QWebPage.WebAction'
    ToggleSubscript = ... # type: 'QWebPage.WebAction'
    ToggleSuperscript = ... # type: 'QWebPage.WebAction'
    InsertUnorderedList = ... # type: 'QWebPage.WebAction'
    InsertOrderedList = ... # type: 'QWebPage.WebAction'
    Indent = ... # type: 'QWebPage.WebAction'
    Outdent = ... # type: 'QWebPage.WebAction'
    AlignCenter = ... # type: 'QWebPage.WebAction'
    AlignJustified = ... # type: 'QWebPage.WebAction'
    AlignLeft = ... # type: 'QWebPage.WebAction'
    AlignRight = ... # type: 'QWebPage.WebAction'
    StopScheduledPageRefresh = ... # type: 'QWebPage.WebAction'
    CopyImageUrlToClipboard = ... # type: 'QWebPage.WebAction'
    OpenLinkInThisWindow = ... # type: 'QWebPage.WebAction'
    DownloadMediaToDisk = ... # type: 'QWebPage.WebAction'
    CopyMediaUrlToClipboard = ... # type: 'QWebPage.WebAction'
    ToggleMediaControls = ... # type: 'QWebPage.WebAction'
    ToggleMediaLoop = ... # type: 'QWebPage.WebAction'
    ToggleMediaPlayPause = ... # type: 'QWebPage.WebAction'
    ToggleMediaMute = ... # type: 'QWebPage.WebAction'
    ToggleVideoFullscreen = ... # type: 'QWebPage.WebAction'

    class NavigationType(int): ...
    NavigationTypeLinkClicked = ... # type: 'QWebPage.NavigationType'
    NavigationTypeFormSubmitted = ... # type: 'QWebPage.NavigationType'
    NavigationTypeBackOrForward = ... # type: 'QWebPage.NavigationType'
    NavigationTypeReload = ... # type: 'QWebPage.NavigationType'
    NavigationTypeFormResubmitted = ... # type: 'QWebPage.NavigationType'
    NavigationTypeOther = ... # type: 'QWebPage.NavigationType'

    class FindFlags(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QWebPage.FindFlags', 'QWebPage.FindFlag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebPage.FindFlags') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QWebPage.FindFlags': ...
        def __int__(self) -> int: ...

    class ExtensionOption(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebPage.ExtensionOption') -> None: ...

    class ExtensionReturn(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebPage.ExtensionReturn') -> None: ...

    class ChooseMultipleFilesExtensionOption('QWebPage.ExtensionOption'):

        parentFrame = ... # type: QWebFrame
        suggestedFileNames = ... # type: typing.Iterable[str]

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebPage.ChooseMultipleFilesExtensionOption') -> None: ...

    class ChooseMultipleFilesExtensionReturn('QWebPage.ExtensionReturn'):

        fileNames = ... # type: typing.Iterable[str]

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebPage.ChooseMultipleFilesExtensionReturn') -> None: ...

    class ErrorPageExtensionOption('QWebPage.ExtensionOption'):

        domain = ... # type: 'QWebPage.ErrorDomain'
        error = ... # type: int
        errorString = ... # type: str
        frame = ... # type: QWebFrame
        url = ... # type: QtCore.QUrl

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebPage.ErrorPageExtensionOption') -> None: ...

    class ErrorPageExtensionReturn('QWebPage.ExtensionReturn'):

        baseUrl = ... # type: QtCore.QUrl
        content = ... # type: typing.Union[QtCore.QByteArray, bytes, bytearray]
        contentType = ... # type: str
        encoding = ... # type: str

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebPage.ErrorPageExtensionReturn') -> None: ...

    class ViewportAttributes(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, other: 'QWebPage.ViewportAttributes') -> None: ...

        def size(self) -> QtCore.QSizeF: ...
        def isValid(self) -> bool: ...
        def isUserScalable(self) -> bool: ...
        def devicePixelRatio(self) -> float: ...
        def maximumScaleFactor(self) -> float: ...
        def minimumScaleFactor(self) -> float: ...
        def initialScaleFactor(self) -> float: ...

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def setVisibilityState(self, a0: 'QWebPage.VisibilityState') -> None: ...
    def visibilityState(self) -> 'QWebPage.VisibilityState': ...
    def featurePermissionRequestCanceled(self, frame: QWebFrame, feature: 'QWebPage.Feature') -> None: ...
    def featurePermissionRequested(self, frame: QWebFrame, feature: 'QWebPage.Feature') -> None: ...
    def viewportChangeRequested(self) -> None: ...
    def applicationCacheQuotaExceeded(self, origin: QtWebKit.QWebSecurityOrigin, defaultOriginQuota: int, totalSpaceNeeded: int) -> None: ...
    def supportsContentType(self, mimeType: str) -> bool: ...
    def supportedContentTypes(self) -> typing.List[str]: ...
    def setFeaturePermission(self, frame: QWebFrame, feature: 'QWebPage.Feature', policy: 'QWebPage.PermissionPolicy') -> None: ...
    def setActualVisibleContentRect(self, rect: QtCore.QRect) -> None: ...
    def viewportAttributesForSize(self, availableSize: QtCore.QSize) -> 'QWebPage.ViewportAttributes': ...
    def selectedHtml(self) -> str: ...
    def hasSelection(self) -> bool: ...
    def shouldInterruptJavaScript(self) -> bool: ...
    def setPreferredContentsSize(self, size: QtCore.QSize) -> None: ...
    def preferredContentsSize(self) -> QtCore.QSize: ...
    def frameAt(self, pos: QtCore.QPoint) -> QWebFrame: ...
    def restoreFrameStateRequested(self, frame: QWebFrame) -> None: ...
    def saveFrameStateRequested(self, frame: QWebFrame, item: QtWebKit.QWebHistoryItem) -> None: ...
    def databaseQuotaExceeded(self, frame: QWebFrame, databaseName: str) -> None: ...
    def contentsChanged(self) -> None: ...
    def createStandardContextMenu(self) -> QtWidgets.QMenu: ...
    def isContentEditable(self) -> bool: ...
    def setContentEditable(self, editable: bool) -> None: ...
    def userAgentForUrl(self, url: QtCore.QUrl) -> str: ...
    def javaScriptConsoleMessage(self, message: str, lineNumber: int, sourceID: str) -> None: ...
    def javaScriptPrompt(self, originatingFrame: QWebFrame, msg: str, defaultValue: str) -> typing.Tuple[bool, str]: ...
    def javaScriptConfirm(self, originatingFrame: QWebFrame, msg: str) -> bool: ...
    def javaScriptAlert(self, originatingFrame: QWebFrame, msg: str) -> None: ...
    def chooseFile(self, originatingFrame: QWebFrame, oldFile: str) -> str: ...
    def acceptNavigationRequest(self, frame: QWebFrame, request: QtNetwork.QNetworkRequest, type: 'QWebPage.NavigationType') -> bool: ...
    def createPlugin(self, classid: str, url: QtCore.QUrl, paramNames: typing.Iterable[str], paramValues: typing.Iterable[str]) -> QtCore.QObject: ...
    def createWindow(self, type: 'QWebPage.WebWindowType') -> 'QWebPage': ...
    def microFocusChanged(self) -> None: ...
    def downloadRequested(self, request: QtNetwork.QNetworkRequest) -> None: ...
    def unsupportedContent(self, reply: QtNetwork.QNetworkReply) -> None: ...
    def menuBarVisibilityChangeRequested(self, visible: bool) -> None: ...
    def statusBarVisibilityChangeRequested(self, visible: bool) -> None: ...
    def toolBarVisibilityChangeRequested(self, visible: bool) -> None: ...
    def linkClicked(self, url: QtCore.QUrl) -> None: ...
    def printRequested(self, frame: QWebFrame) -> None: ...
    def windowCloseRequested(self) -> None: ...
    def scrollRequested(self, dx: int, dy: int, scrollViewRect: QtCore.QRect) -> None: ...
    def repaintRequested(self, dirtyRect: QtCore.QRect) -> None: ...
    def geometryChangeRequested(self, geom: QtCore.QRect) -> None: ...
    def frameCreated(self, frame: QWebFrame) -> None: ...
    def selectionChanged(self) -> None: ...
    def statusBarMessage(self, text: str) -> None: ...
    def linkHovered(self, link: str, title: str, textContent: str) -> None: ...
    def loadStarted(self) -> None: ...
    def loadProgress(self, progress: int) -> None: ...
    def loadFinished(self, ok: bool) -> None: ...
    def supportsExtension(self, extension: 'QWebPage.Extension') -> bool: ...
    def extension(self, extension: 'QWebPage.Extension', option: typing.Optional['QWebPage.ExtensionOption'] = ..., output: typing.Optional['QWebPage.ExtensionReturn'] = ...) -> bool: ...
    def updatePositionDependentActions(self, pos: QtCore.QPoint) -> None: ...
    def swallowContextMenuEvent(self, event: QtGui.QContextMenuEvent) -> bool: ...
    def palette(self) -> QtGui.QPalette: ...
    def setPalette(self, palette: QtGui.QPalette) -> None: ...
    def linkDelegationPolicy(self) -> 'QWebPage.LinkDelegationPolicy': ...
    def setLinkDelegationPolicy(self, policy: 'QWebPage.LinkDelegationPolicy') -> None: ...
    def forwardUnsupportedContent(self) -> bool: ...
    def setForwardUnsupportedContent(self, forward: bool) -> None: ...
    def findText(self, subString: str, options: 'QWebPage.FindFlags' = ...) -> bool: ...
    def inputMethodQuery(self, property: QtCore.Qt.InputMethodQuery) -> typing.Any: ...
    def focusNextPrevChild(self, next: bool) -> bool: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def setViewportSize(self, size: QtCore.QSize) -> None: ...
    def viewportSize(self) -> QtCore.QSize: ...
    def triggerAction(self, action: 'QWebPage.WebAction', checked: bool = ...) -> None: ...
    def action(self, action: 'QWebPage.WebAction') -> QtWidgets.QAction: ...
    def selectedText(self) -> str: ...
    def bytesReceived(self) -> int: ...
    def totalBytes(self) -> int: ...
    def pluginFactory(self) -> QtWebKit.QWebPluginFactory: ...
    def setPluginFactory(self, factory: QtWebKit.QWebPluginFactory) -> None: ...
    def networkAccessManager(self) -> QtNetwork.QNetworkAccessManager: ...
    def setNetworkAccessManager(self, manager: QtNetwork.QNetworkAccessManager) -> None: ...
    def undoStack(self) -> QtWidgets.QUndoStack: ...
    def isModified(self) -> bool: ...
    def view(self) -> QtWidgets.QWidget: ...
    def setView(self, view: QtWidgets.QWidget) -> None: ...
    def settings(self) -> QtWebKit.QWebSettings: ...
    def history(self) -> QtWebKit.QWebHistory: ...
    def currentFrame(self) -> QWebFrame: ...
    def mainFrame(self) -> QWebFrame: ...


class QWebView(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def selectedHtml(self) -> str: ...
    def hasSelection(self) -> bool: ...
    def setRenderHint(self, hint: QtGui.QPainter.RenderHint, enabled: bool = ...) -> None: ...
    def setRenderHints(self, hints: QtGui.QPainter.RenderHints) -> None: ...
    def renderHints(self) -> QtGui.QPainter.RenderHints: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def zoomFactor(self) -> float: ...
    def focusNextPrevChild(self, next: bool) -> bool: ...
    def inputMethodEvent(self, a0: QtGui.QInputMethodEvent) -> None: ...
    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None: ...
    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None: ...
    def dropEvent(self, a0: QtGui.QDropEvent) -> None: ...
    def dragMoveEvent(self, a0: QtGui.QDragMoveEvent) -> None: ...
    def dragLeaveEvent(self, a0: QtGui.QDragLeaveEvent) -> None: ...
    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None: ...
    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None: ...
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None: ...
    def wheelEvent(self, a0: QtGui.QWheelEvent) -> None: ...
    def contextMenuEvent(self, a0: QtGui.QContextMenuEvent) -> None: ...
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def changeEvent(self, a0: QtCore.QEvent) -> None: ...
    def paintEvent(self, ev: QtGui.QPaintEvent) -> None: ...
    def resizeEvent(self, e: QtGui.QResizeEvent) -> None: ...
    def createWindow(self, type: QWebPage.WebWindowType) -> 'QWebView': ...
    def urlChanged(self, url: QtCore.QUrl) -> None: ...
    def iconChanged(self) -> None: ...
    def selectionChanged(self) -> None: ...
    def linkClicked(self, url: QtCore.QUrl) -> None: ...
    def statusBarMessage(self, text: str) -> None: ...
    def titleChanged(self, title: str) -> None: ...
    def loadFinished(self, a0: bool) -> None: ...
    def loadProgress(self, progress: int) -> None: ...
    def loadStarted(self) -> None: ...
    def print(self, printer: QtPrintSupport.QPrinter) -> None: ...
    def print_(self, printer: QtPrintSupport.QPrinter) -> None: ...
    def reload(self) -> None: ...
    def forward(self) -> None: ...
    def back(self) -> None: ...
    def stop(self) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def findText(self, subString: str, options: QWebPage.FindFlags = ...) -> bool: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def inputMethodQuery(self, property: QtCore.Qt.InputMethodQuery) -> typing.Any: ...
    def isModified(self) -> bool: ...
    def triggerPageAction(self, action: QWebPage.WebAction, checked: bool = ...) -> None: ...
    def pageAction(self, action: QWebPage.WebAction) -> QtWidgets.QAction: ...
    def selectedText(self) -> str: ...
    def icon(self) -> QtGui.QIcon: ...
    def url(self) -> QtCore.QUrl: ...
    def setUrl(self, url: QtCore.QUrl) -> None: ...
    def title(self) -> str: ...
    def settings(self) -> QtWebKit.QWebSettings: ...
    def history(self) -> QtWebKit.QWebHistory: ...
    def setContent(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], mimeType: str = ..., baseUrl: QtCore.QUrl = ...) -> None: ...
    def setHtml(self, html: str, baseUrl: QtCore.QUrl = ...) -> None: ...
    @typing.overload
    def load(self, url: QtCore.QUrl) -> None: ...
    @typing.overload
    def load(self, request: QtNetwork.QNetworkRequest, operation: QtNetwork.QNetworkAccessManager.Operation = ..., body: typing.Union[QtCore.QByteArray, bytes, bytearray] = ...) -> None: ...
    def setPage(self, page: QWebPage) -> None: ...
    def page(self) -> QWebPage: ...