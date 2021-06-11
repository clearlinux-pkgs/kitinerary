#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kitinerary
Version  : 21.04.2
Release  : 36
URL      : https://download.kde.org/stable/release-service/21.04.2/src/kitinerary-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/kitinerary-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/kitinerary-21.04.2.tar.xz.sig
Summary  : Data model and extraction system for travel reservation information
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kitinerary-data = %{version}-%{release}
Requires: kitinerary-lib = %{version}-%{release}
Requires: kitinerary-license = %{version}-%{release}
Requires: kitinerary-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(poppler)
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : kpkpass-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : poppler-dev
BuildRequires : qtbase-dev
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
%setup -q -n kitinerary-21.04.2
cd %{_builddir}/kitinerary-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623389832
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623389832
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kitinerary
cp %{_builddir}/kitinerary-21.04.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kitinerary/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kitinerary-21.04.2/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kitinerary/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kitinerary-21.04.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kitinerary/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kitinerary-21.04.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kitinerary/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kitinerary-21.04.2/README.md.license %{buildroot}/usr/share/package-licenses/kitinerary/fca67987925d2ed70e898f6dd9c7fe4b458d416d
cp %{_builddir}/kitinerary-21.04.2/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kitinerary/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang kitinerary

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/kitinerary-extractor

%files data
%defattr(-,root,root,-)
/usr/share/mime-packages/application-vnd-kde-itinerary.xml
/usr/share/qlogging-categories5/org_kde_kitinerary.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim/KItinerary/Action
/usr/include/KPim/KItinerary/AlphaId
/usr/include/KPim/KItinerary/BarcodeDecoder
/usr/include/KPim/KItinerary/Brand
/usr/include/KPim/KItinerary/BusTrip
/usr/include/KPim/KItinerary/CalendarHandler
/usr/include/KPim/KItinerary/CountryDb
/usr/include/KPim/KItinerary/CreativeWork
/usr/include/KPim/KItinerary/Datatypes
/usr/include/KPim/KItinerary/DocumentUtil
/usr/include/KPim/KItinerary/Event
/usr/include/KPim/KItinerary/Extractor
/usr/include/KPim/KItinerary/ExtractorCapabilities
/usr/include/KPim/KItinerary/ExtractorEngine
/usr/include/KPim/KItinerary/ExtractorFilter
/usr/include/KPim/KItinerary/ExtractorInput
/usr/include/KPim/KItinerary/ExtractorPostprocessor
/usr/include/KPim/KItinerary/ExtractorRepository
/usr/include/KPim/KItinerary/ExtractorValidator
/usr/include/KPim/KItinerary/File
/usr/include/KPim/KItinerary/Flight
/usr/include/KPim/KItinerary/HtmlDocument
/usr/include/KPim/KItinerary/IataBcbpParser
/usr/include/KPim/KItinerary/JsonLdDocument
/usr/include/KPim/KItinerary/KnowledgeDb
/usr/include/KPim/KItinerary/LocationUtil
/usr/include/KPim/KItinerary/MergeUtil
/usr/include/KPim/KItinerary/Organization
/usr/include/KPim/KItinerary/PdfDocument
/usr/include/KPim/KItinerary/PdfImage
/usr/include/KPim/KItinerary/Person
/usr/include/KPim/KItinerary/Place
/usr/include/KPim/KItinerary/Rct2Ticket
/usr/include/KPim/KItinerary/RentalCar
/usr/include/KPim/KItinerary/Reservation
/usr/include/KPim/KItinerary/SortUtil
/usr/include/KPim/KItinerary/Taxi
/usr/include/KPim/KItinerary/Ticket
/usr/include/KPim/KItinerary/TrainTrip
/usr/include/KPim/KItinerary/Uic9183Block
/usr/include/KPim/KItinerary/Uic9183Parser
/usr/include/KPim/KItinerary/Uic9183TicketLayout
/usr/include/KPim/KItinerary/Uic9183Utils
/usr/include/KPim/KItinerary/VdvTicket
/usr/include/KPim/KItinerary/VdvTicketParser
/usr/include/KPim/KItinerary/Vendor0080Block
/usr/include/KPim/KItinerary/Visit
/usr/include/KPim/kitinerary/action.h
/usr/include/KPim/kitinerary/alphaid.h
/usr/include/KPim/kitinerary/barcodedecoder.h
/usr/include/KPim/kitinerary/brand.h
/usr/include/KPim/kitinerary/bustrip.h
/usr/include/KPim/kitinerary/calendarhandler.h
/usr/include/KPim/kitinerary/countrydb.h
/usr/include/KPim/kitinerary/creativework.h
/usr/include/KPim/kitinerary/datatypes.h
/usr/include/KPim/kitinerary/documentutil.h
/usr/include/KPim/kitinerary/event.h
/usr/include/KPim/kitinerary/extractor.h
/usr/include/KPim/kitinerary/extractorcapabilities.h
/usr/include/KPim/kitinerary/extractorengine.h
/usr/include/KPim/kitinerary/extractorfilter.h
/usr/include/KPim/kitinerary/extractorinput.h
/usr/include/KPim/kitinerary/extractorpostprocessor.h
/usr/include/KPim/kitinerary/extractorrepository.h
/usr/include/KPim/kitinerary/extractorvalidator.h
/usr/include/KPim/kitinerary/file.h
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
/usr/include/KPim/kitinerary/pdfimage.h
/usr/include/KPim/kitinerary/person.h
/usr/include/KPim/kitinerary/place.h
/usr/include/KPim/kitinerary/rct2ticket.h
/usr/include/KPim/kitinerary/rentalcar.h
/usr/include/KPim/kitinerary/reservation.h
/usr/include/KPim/kitinerary/sortutil.h
/usr/include/KPim/kitinerary/taxi.h
/usr/include/KPim/kitinerary/ticket.h
/usr/include/KPim/kitinerary/traintrip.h
/usr/include/KPim/kitinerary/uic9183block.h
/usr/include/KPim/kitinerary/uic9183parser.h
/usr/include/KPim/kitinerary/uic9183ticketlayout.h
/usr/include/KPim/kitinerary/uic9183utils.h
/usr/include/KPim/kitinerary/vdvticket.h
/usr/include/KPim/kitinerary/vdvticketparser.h
/usr/include/KPim/kitinerary/vendor0080block.h
/usr/include/KPim/kitinerary/visit.h
/usr/include/KPim/kitinerary_version.h
/usr/lib64/cmake/KPimItinerary/KPimItineraryConfig.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryConfigVersion.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryTargets.cmake
/usr/lib64/libKPimItinerary.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPimItinerary.so.5
/usr/lib64/libKPimItinerary.so.5.17.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kitinerary/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kitinerary/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kitinerary/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kitinerary/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kitinerary/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kitinerary/fca67987925d2ed70e898f6dd9c7fe4b458d416d

%files locales -f kitinerary.lang
%defattr(-,root,root,-)

