#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kitinerary
Version  : 19.04.0
Release  : 8
URL      : https://download.kde.org/stable/applications/19.04.0/src/kitinerary-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/kitinerary-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/kitinerary-19.04.0.tar.xz.sig
Summary  : Data model and extraction system for travel reservation information
Group    : Development/Tools
License  : LGPL-2.1
Requires: kitinerary-data = %{version}-%{release}
Requires: kitinerary-lib = %{version}-%{release}
Requires: kitinerary-license = %{version}-%{release}
Requires: kitinerary-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(poppler)
BuildRequires : kcalcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : kpkpass-dev
BuildRequires : libxml2-dev
BuildRequires : poppler-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : zlib-dev

%description
Development tip: symlink this folder to $PREFIX/share/kitinerary/extractors
It will then take priority over the compiled-in files allowing you to test
script changes without recompilation.

%package data
Summary: data components for the kitinerary package.
Group: Data

%description data
data components for the kitinerary package.


%package dev
Summary: dev components for the kitinerary package.
Group: Development
Requires: kitinerary-lib = %{version}-%{release}
Requires: kitinerary-data = %{version}-%{release}
Provides: kitinerary-devel = %{version}-%{release}
Requires: kitinerary = %{version}-%{release}

%description dev
dev components for the kitinerary package.


%package lib
Summary: lib components for the kitinerary package.
Group: Libraries
Requires: kitinerary-data = %{version}-%{release}
Requires: kitinerary-license = %{version}-%{release}

%description lib
lib components for the kitinerary package.


%package license
Summary: license components for the kitinerary package.
Group: Default

%description license
license components for the kitinerary package.


%package locales
Summary: locales components for the kitinerary package.
Group: Default

%description locales
locales components for the kitinerary package.


%prep
%setup -q -n kitinerary-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555634221
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555634221
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kitinerary
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kitinerary/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kitinerary

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/kitinerary-extractor

%files data
%defattr(-,root,root,-)
/usr/share/xdg/org_kde_kitinerary.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim/KItinerary/Action
/usr/include/KPim/KItinerary/BarcodeDecoder
/usr/include/KPim/KItinerary/Brand
/usr/include/KPim/KItinerary/BusTrip
/usr/include/KPim/KItinerary/CalendarHandler
/usr/include/KPim/KItinerary/CountryDb
/usr/include/KPim/KItinerary/Datatypes
/usr/include/KPim/KItinerary/Event
/usr/include/KPim/KItinerary/Extractor
/usr/include/KPim/KItinerary/ExtractorEngine
/usr/include/KPim/KItinerary/ExtractorPostprocessor
/usr/include/KPim/KItinerary/Flight
/usr/include/KPim/KItinerary/HtmlDocument
/usr/include/KPim/KItinerary/IataBcbpParser
/usr/include/KPim/KItinerary/JsonLdDocument
/usr/include/KPim/KItinerary/KnowledgeDb
/usr/include/KPim/KItinerary/LocationUtil
/usr/include/KPim/KItinerary/MergeUtil
/usr/include/KPim/KItinerary/Organization
/usr/include/KPim/KItinerary/PdfDocument
/usr/include/KPim/KItinerary/Person
/usr/include/KPim/KItinerary/Place
/usr/include/KPim/KItinerary/Rct2Ticket
/usr/include/KPim/KItinerary/RentalCar
/usr/include/KPim/KItinerary/Reservation
/usr/include/KPim/KItinerary/SortUtil
/usr/include/KPim/KItinerary/Taxi
/usr/include/KPim/KItinerary/Ticket
/usr/include/KPim/KItinerary/TrainTrip
/usr/include/KPim/KItinerary/Uic9183Parser
/usr/include/KPim/KItinerary/Visit
/usr/include/KPim/kitinerary/action.h
/usr/include/KPim/kitinerary/barcodedecoder.h
/usr/include/KPim/kitinerary/brand.h
/usr/include/KPim/kitinerary/bustrip.h
/usr/include/KPim/kitinerary/calendarhandler.h
/usr/include/KPim/kitinerary/countrydb.h
/usr/include/KPim/kitinerary/datatypes.h
/usr/include/KPim/kitinerary/event.h
/usr/include/KPim/kitinerary/extractor.h
/usr/include/KPim/kitinerary/extractorengine.h
/usr/include/KPim/kitinerary/extractorpostprocessor.h
/usr/include/KPim/kitinerary/flight.h
/usr/include/KPim/kitinerary/htmldocument.h
/usr/include/KPim/kitinerary/iatabcbpparser.h
/usr/include/KPim/kitinerary/jsonlddocument.h
/usr/include/KPim/kitinerary/kitinerary_export.h
/usr/include/KPim/kitinerary/knowledgedb.h
/usr/include/KPim/kitinerary/locationutil.h
/usr/include/KPim/kitinerary/mergeutil.h
/usr/include/KPim/kitinerary/organization.h
/usr/include/KPim/kitinerary/pdfdocument.h
/usr/include/KPim/kitinerary/person.h
/usr/include/KPim/kitinerary/place.h
/usr/include/KPim/kitinerary/rct2ticket.h
/usr/include/KPim/kitinerary/rentalcar.h
/usr/include/KPim/kitinerary/reservation.h
/usr/include/KPim/kitinerary/sortutil.h
/usr/include/KPim/kitinerary/taxi.h
/usr/include/KPim/kitinerary/ticket.h
/usr/include/KPim/kitinerary/traintrip.h
/usr/include/KPim/kitinerary/uic9183parser.h
/usr/include/KPim/kitinerary/visit.h
/usr/lib64/cmake/KPimItinerary/KPimItineraryConfig.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryConfigVersion.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryTargets.cmake
/usr/lib64/libKPimItinerary.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPimItinerary.so.5
/usr/lib64/libKPimItinerary.so.5.11.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kitinerary/COPYING.LIB

%files locales -f kitinerary.lang
%defattr(-,root,root,-)

