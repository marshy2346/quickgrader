# The PEP 484 type hints stub file for the QtPositioning module.
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

from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QGeoAddress(sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoAddress') -> None: ...

    def isTextGenerated(self) -> bool: ...
    def clear(self) -> None: ...
    def isEmpty(self) -> bool: ...
    def setStreet(self, street: str) -> None: ...
    def street(self) -> str: ...
    def setPostalCode(self, postalCode: str) -> None: ...
    def postalCode(self) -> str: ...
    def setDistrict(self, district: str) -> None: ...
    def district(self) -> str: ...
    def setCity(self, city: str) -> None: ...
    def city(self) -> str: ...
    def setCounty(self, county: str) -> None: ...
    def county(self) -> str: ...
    def setState(self, state: str) -> None: ...
    def state(self) -> str: ...
    def setCountryCode(self, countryCode: str) -> None: ...
    def countryCode(self) -> str: ...
    def setCountry(self, country: str) -> None: ...
    def country(self) -> str: ...
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...


class QGeoAreaMonitorInfo(sip.wrapper):

    @typing.overload
    def __init__(self, name: str = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoAreaMonitorInfo') -> None: ...

    def setNotificationParameters(self, parameters: typing.Dict[str, typing.Any]) -> None: ...
    def notificationParameters(self) -> typing.Dict[str, typing.Any]: ...
    def setPersistent(self, isPersistent: bool) -> None: ...
    def isPersistent(self) -> bool: ...
    def setExpiration(self, expiry: typing.Union[QtCore.QDateTime, datetime.datetime]) -> None: ...
    def expiration(self) -> QtCore.QDateTime: ...
    def setArea(self, newShape: 'QGeoShape') -> None: ...
    def area(self) -> 'QGeoShape': ...
    def isValid(self) -> bool: ...
    def identifier(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def name(self) -> str: ...


class QGeoAreaMonitorSource(QtCore.QObject):

    class AreaMonitorFeature(int): ...
    PersistentAreaMonitorFeature = ... # type: 'QGeoAreaMonitorSource.AreaMonitorFeature'
    AnyAreaMonitorFeature = ... # type: 'QGeoAreaMonitorSource.AreaMonitorFeature'

    class Error(int): ...
    AccessError = ... # type: 'QGeoAreaMonitorSource.Error'
    InsufficientPositionInfo = ... # type: 'QGeoAreaMonitorSource.Error'
    UnknownSourceError = ... # type: 'QGeoAreaMonitorSource.Error'
    NoError = ... # type: 'QGeoAreaMonitorSource.Error'

    class AreaMonitorFeatures(sip.wrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGeoAreaMonitorSource.AreaMonitorFeatures', 'QGeoAreaMonitorSource.AreaMonitorFeature']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGeoAreaMonitorSource.AreaMonitorFeatures') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGeoAreaMonitorSource.AreaMonitorFeatures': ...
        def __int__(self) -> int: ...

    def __init__(self, parent: QtCore.QObject) -> None: ...

    def monitorExpired(self, monitor: QGeoAreaMonitorInfo) -> None: ...
    def areaExited(self, monitor: QGeoAreaMonitorInfo, update: 'QGeoPositionInfo') -> None: ...
    def areaEntered(self, monitor: QGeoAreaMonitorInfo, update: 'QGeoPositionInfo') -> None: ...
    @typing.overload
    def activeMonitors(self) -> typing.Any: ...
    @typing.overload
    def activeMonitors(self, lookupArea: 'QGeoShape') -> typing.List[QGeoAreaMonitorInfo]: ...
    def requestUpdate(self, monitor: QGeoAreaMonitorInfo, signal: str) -> bool: ...
    def stopMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool: ...
    def startMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool: ...
    def supportedAreaMonitorFeatures(self) -> 'QGeoAreaMonitorSource.AreaMonitorFeatures': ...
    @typing.overload
    def error(self) -> 'QGeoAreaMonitorSource.Error': ...
    @typing.overload
    def error(self, error: 'QGeoAreaMonitorSource.Error') -> None: ...
    def sourceName(self) -> str: ...
    def positionInfoSource(self) -> 'QGeoPositionInfoSource': ...
    def setPositionInfoSource(self, source: 'QGeoPositionInfoSource') -> None: ...
    @staticmethod
    def availableSources() -> typing.List[str]: ...
    @staticmethod
    def createSource(sourceName: str, parent: QtCore.QObject) -> 'QGeoAreaMonitorSource': ...
    @staticmethod
    def createDefaultSource(parent: QtCore.QObject) -> 'QGeoAreaMonitorSource': ...


class QGeoShape(sip.wrapper):

    class ShapeType(int): ...
    UnknownType = ... # type: 'QGeoShape.ShapeType'
    RectangleType = ... # type: 'QGeoShape.ShapeType'
    CircleType = ... # type: 'QGeoShape.ShapeType'
    PathType = ... # type: 'QGeoShape.ShapeType'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoShape') -> None: ...

    def boundingGeoRectangle(self) -> 'QGeoRectangle': ...
    def toString(self) -> str: ...
    def center(self) -> 'QGeoCoordinate': ...
    def extendShape(self, coordinate: 'QGeoCoordinate') -> None: ...
    def contains(self, coordinate: 'QGeoCoordinate') -> bool: ...
    def isEmpty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def type(self) -> 'QGeoShape.ShapeType': ...


class QGeoCircle(QGeoShape):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, center: 'QGeoCoordinate', radius: float = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoCircle') -> None: ...
    @typing.overload
    def __init__(self, other: QGeoShape) -> None: ...

    def extendCircle(self, coordinate: 'QGeoCoordinate') -> None: ...
    def toString(self) -> str: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> 'QGeoCircle': ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def radius(self) -> float: ...
    def setRadius(self, radius: float) -> None: ...
    def center(self) -> 'QGeoCoordinate': ...
    def setCenter(self, center: 'QGeoCoordinate') -> None: ...


class QGeoCoordinate(sip.wrapper):

    class CoordinateFormat(int): ...
    Degrees = ... # type: 'QGeoCoordinate.CoordinateFormat'
    DegreesWithHemisphere = ... # type: 'QGeoCoordinate.CoordinateFormat'
    DegreesMinutes = ... # type: 'QGeoCoordinate.CoordinateFormat'
    DegreesMinutesWithHemisphere = ... # type: 'QGeoCoordinate.CoordinateFormat'
    DegreesMinutesSeconds = ... # type: 'QGeoCoordinate.CoordinateFormat'
    DegreesMinutesSecondsWithHemisphere = ... # type: 'QGeoCoordinate.CoordinateFormat'

    class CoordinateType(int): ...
    InvalidCoordinate = ... # type: 'QGeoCoordinate.CoordinateType'
    Coordinate2D = ... # type: 'QGeoCoordinate.CoordinateType'
    Coordinate3D = ... # type: 'QGeoCoordinate.CoordinateType'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, latitude: float, longitude: float) -> None: ...
    @typing.overload
    def __init__(self, latitude: float, longitude: float, altitude: float) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoCoordinate') -> None: ...

    def __hash__(self) -> int: ...
    def toString(self, format: 'QGeoCoordinate.CoordinateFormat' = ...) -> str: ...
    def atDistanceAndAzimuth(self, distance: float, azimuth: float, distanceUp: float = ...) -> 'QGeoCoordinate': ...
    def azimuthTo(self, other: 'QGeoCoordinate') -> float: ...
    def distanceTo(self, other: 'QGeoCoordinate') -> float: ...
    def altitude(self) -> float: ...
    def setAltitude(self, altitude: float) -> None: ...
    def longitude(self) -> float: ...
    def setLongitude(self, longitude: float) -> None: ...
    def latitude(self) -> float: ...
    def setLatitude(self, latitude: float) -> None: ...
    def type(self) -> 'QGeoCoordinate.CoordinateType': ...
    def isValid(self) -> bool: ...


class QGeoLocation(sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoLocation') -> None: ...

    def isEmpty(self) -> bool: ...
    def setBoundingBox(self, box: 'QGeoRectangle') -> None: ...
    def boundingBox(self) -> 'QGeoRectangle': ...
    def setCoordinate(self, position: QGeoCoordinate) -> None: ...
    def coordinate(self) -> QGeoCoordinate: ...
    def setAddress(self, address: QGeoAddress) -> None: ...
    def address(self) -> QGeoAddress: ...


class QGeoPath(QGeoShape):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, path: typing.Any, width: float = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoPath') -> None: ...
    @typing.overload
    def __init__(self, other: QGeoShape) -> None: ...

    def toString(self) -> str: ...
    @typing.overload
    def removeCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    @typing.overload
    def removeCoordinate(self, index: int) -> None: ...
    def containsCoordinate(self, coordinate: QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index: int) -> QGeoCoordinate: ...
    def replaceCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None: ...
    def insertCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None: ...
    def addCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    def length(self, indexFrom: int = ..., indexTo: int = ...) -> float: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> 'QGeoPath': ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def width(self) -> float: ...
    def setWidth(self, width: float) -> None: ...
    def path(self) -> typing.List[QGeoCoordinate]: ...
    def setPath(self, path: typing.Iterable[QGeoCoordinate]) -> None: ...


class QGeoPositionInfo(sip.wrapper):

    class Attribute(int): ...
    Direction = ... # type: 'QGeoPositionInfo.Attribute'
    GroundSpeed = ... # type: 'QGeoPositionInfo.Attribute'
    VerticalSpeed = ... # type: 'QGeoPositionInfo.Attribute'
    MagneticVariation = ... # type: 'QGeoPositionInfo.Attribute'
    HorizontalAccuracy = ... # type: 'QGeoPositionInfo.Attribute'
    VerticalAccuracy = ... # type: 'QGeoPositionInfo.Attribute'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, coordinate: QGeoCoordinate, updateTime: typing.Union[QtCore.QDateTime, datetime.datetime]) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoPositionInfo') -> None: ...

    def hasAttribute(self, attribute: 'QGeoPositionInfo.Attribute') -> bool: ...
    def removeAttribute(self, attribute: 'QGeoPositionInfo.Attribute') -> None: ...
    def attribute(self, attribute: 'QGeoPositionInfo.Attribute') -> float: ...
    def setAttribute(self, attribute: 'QGeoPositionInfo.Attribute', value: float) -> None: ...
    def coordinate(self) -> QGeoCoordinate: ...
    def setCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    def timestamp(self) -> QtCore.QDateTime: ...
    def setTimestamp(self, timestamp: typing.Union[QtCore.QDateTime, datetime.datetime]) -> None: ...
    def isValid(self) -> bool: ...


class QGeoPositionInfoSource(QtCore.QObject):

    class PositioningMethod(int): ...
    NoPositioningMethods = ... # type: 'QGeoPositionInfoSource.PositioningMethod'
    SatellitePositioningMethods = ... # type: 'QGeoPositionInfoSource.PositioningMethod'
    NonSatellitePositioningMethods = ... # type: 'QGeoPositionInfoSource.PositioningMethod'
    AllPositioningMethods = ... # type: 'QGeoPositionInfoSource.PositioningMethod'

    class Error(int): ...
    AccessError = ... # type: 'QGeoPositionInfoSource.Error'
    ClosedError = ... # type: 'QGeoPositionInfoSource.Error'
    UnknownSourceError = ... # type: 'QGeoPositionInfoSource.Error'
    NoError = ... # type: 'QGeoPositionInfoSource.Error'

    class PositioningMethods(sip.wrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QGeoPositionInfoSource.PositioningMethods', 'QGeoPositionInfoSource.PositioningMethod']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QGeoPositionInfoSource.PositioningMethods') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QGeoPositionInfoSource.PositioningMethods': ...
        def __int__(self) -> int: ...

    def __init__(self, parent: QtCore.QObject) -> None: ...

    def updateTimeout(self) -> None: ...
    def positionUpdated(self, update: QGeoPositionInfo) -> None: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def stopUpdates(self) -> None: ...
    def startUpdates(self) -> None: ...
    @typing.overload
    def error(self) -> 'QGeoPositionInfoSource.Error': ...
    @typing.overload
    def error(self, a0: 'QGeoPositionInfoSource.Error') -> None: ...
    @staticmethod
    def availableSources() -> typing.List[str]: ...
    @staticmethod
    def createSource(sourceName: str, parent: QtCore.QObject) -> 'QGeoPositionInfoSource': ...
    @staticmethod
    def createDefaultSource(parent: QtCore.QObject) -> 'QGeoPositionInfoSource': ...
    def sourceName(self) -> str: ...
    def minimumUpdateInterval(self) -> int: ...
    def supportedPositioningMethods(self) -> 'QGeoPositionInfoSource.PositioningMethods': ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = ...) -> QGeoPositionInfo: ...
    def preferredPositioningMethods(self) -> 'QGeoPositionInfoSource.PositioningMethods': ...
    def setPreferredPositioningMethods(self, methods: 'QGeoPositionInfoSource.PositioningMethods') -> None: ...
    def updateInterval(self) -> int: ...
    def setUpdateInterval(self, msec: int) -> None: ...


class QGeoRectangle(QGeoShape):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, center: QGeoCoordinate, degreesWidth: float, degreesHeight: float) -> None: ...
    @typing.overload
    def __init__(self, topLeft: QGeoCoordinate, bottomRight: QGeoCoordinate) -> None: ...
    @typing.overload
    def __init__(self, coordinates: typing.Iterable[QGeoCoordinate]) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoRectangle') -> None: ...
    @typing.overload
    def __init__(self, other: QGeoShape) -> None: ...

    def extendRectangle(self, coordinate: QGeoCoordinate) -> None: ...
    def toString(self) -> str: ...
    def united(self, rectangle: 'QGeoRectangle') -> 'QGeoRectangle': ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> 'QGeoRectangle': ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def intersects(self, rectangle: 'QGeoRectangle') -> bool: ...
    def contains(self, rectangle: 'QGeoRectangle') -> bool: ...
    def height(self) -> float: ...
    def setHeight(self, degreesHeight: float) -> None: ...
    def width(self) -> float: ...
    def setWidth(self, degreesWidth: float) -> None: ...
    def center(self) -> QGeoCoordinate: ...
    def setCenter(self, center: QGeoCoordinate) -> None: ...
    def bottomRight(self) -> QGeoCoordinate: ...
    def setBottomRight(self, bottomRight: QGeoCoordinate) -> None: ...
    def bottomLeft(self) -> QGeoCoordinate: ...
    def setBottomLeft(self, bottomLeft: QGeoCoordinate) -> None: ...
    def topRight(self) -> QGeoCoordinate: ...
    def setTopRight(self, topRight: QGeoCoordinate) -> None: ...
    def topLeft(self) -> QGeoCoordinate: ...
    def setTopLeft(self, topLeft: QGeoCoordinate) -> None: ...


class QGeoSatelliteInfo(sip.wrapper):

    class SatelliteSystem(int): ...
    Undefined = ... # type: 'QGeoSatelliteInfo.SatelliteSystem'
    GPS = ... # type: 'QGeoSatelliteInfo.SatelliteSystem'
    GLONASS = ... # type: 'QGeoSatelliteInfo.SatelliteSystem'

    class Attribute(int): ...
    Elevation = ... # type: 'QGeoSatelliteInfo.Attribute'
    Azimuth = ... # type: 'QGeoSatelliteInfo.Attribute'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoSatelliteInfo') -> None: ...

    def hasAttribute(self, attribute: 'QGeoSatelliteInfo.Attribute') -> bool: ...
    def removeAttribute(self, attribute: 'QGeoSatelliteInfo.Attribute') -> None: ...
    def attribute(self, attribute: 'QGeoSatelliteInfo.Attribute') -> float: ...
    def setAttribute(self, attribute: 'QGeoSatelliteInfo.Attribute', value: float) -> None: ...
    def signalStrength(self) -> int: ...
    def setSignalStrength(self, signalStrength: int) -> None: ...
    def satelliteIdentifier(self) -> int: ...
    def setSatelliteIdentifier(self, satId: int) -> None: ...
    def satelliteSystem(self) -> 'QGeoSatelliteInfo.SatelliteSystem': ...
    def setSatelliteSystem(self, system: 'QGeoSatelliteInfo.SatelliteSystem') -> None: ...


class QGeoSatelliteInfoSource(QtCore.QObject):

    class Error(int): ...
    AccessError = ... # type: 'QGeoSatelliteInfoSource.Error'
    ClosedError = ... # type: 'QGeoSatelliteInfoSource.Error'
    NoError = ... # type: 'QGeoSatelliteInfoSource.Error'
    UnknownSourceError = ... # type: 'QGeoSatelliteInfoSource.Error'

    def __init__(self, parent: QtCore.QObject) -> None: ...

    def requestTimeout(self) -> None: ...
    def satellitesInUseUpdated(self, satellites: typing.Iterable[QGeoSatelliteInfo]) -> None: ...
    def satellitesInViewUpdated(self, satellites: typing.Any) -> None: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def stopUpdates(self) -> None: ...
    def startUpdates(self) -> None: ...
    @typing.overload
    def error(self) -> 'QGeoSatelliteInfoSource.Error': ...
    @typing.overload
    def error(self, a0: 'QGeoSatelliteInfoSource.Error') -> None: ...
    def minimumUpdateInterval(self) -> int: ...
    def updateInterval(self) -> int: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def sourceName(self) -> str: ...
    @staticmethod
    def availableSources() -> typing.List[str]: ...
    @staticmethod
    def createSource(sourceName: str, parent: QtCore.QObject) -> 'QGeoSatelliteInfoSource': ...
    @staticmethod
    def createDefaultSource(parent: QtCore.QObject) -> 'QGeoSatelliteInfoSource': ...


class QNmeaPositionInfoSource(QGeoPositionInfoSource):

    class UpdateMode(int): ...
    RealTimeMode = ... # type: 'QNmeaPositionInfoSource.UpdateMode'
    SimulationMode = ... # type: 'QNmeaPositionInfoSource.UpdateMode'

    def __init__(self, updateMode: 'QNmeaPositionInfoSource.UpdateMode', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def userEquivalentRangeError(self) -> float: ...
    def setUserEquivalentRangeError(self, uere: float) -> None: ...
    def parsePosInfoFromNmeaData(self, data: str, size: int, posInfo: QGeoPositionInfo) -> typing.Tuple[bool, bool]: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def stopUpdates(self) -> None: ...
    def startUpdates(self) -> None: ...
    def error(self) -> QGeoPositionInfoSource.Error: ...
    def minimumUpdateInterval(self) -> int: ...
    def supportedPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethods: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = ...) -> QGeoPositionInfo: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def device(self) -> QtCore.QIODevice: ...
    def setDevice(self, source: QtCore.QIODevice) -> None: ...
    def updateMode(self) -> 'QNmeaPositionInfoSource.UpdateMode': ...
