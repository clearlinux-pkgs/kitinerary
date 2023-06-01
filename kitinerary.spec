#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kitinerary
Version  : 23.04.1
Release  : 89
URL      : https://download.kde.org/stable/release-service/23.04.1/src/kitinerary-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/kitinerary-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/kitinerary-23.04.1.tar.xz.sig
Summary  : Data model and extraction system for travel reservation information
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 LGPL-2.0 ODbL-1.0
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
BuildRequires : zlib-dev
BuildRequires : zxing-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kitinerary-23.04.1
cd %{_builddir}/kitinerary-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685583721
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685583721
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kitinerary
cp %{_builddir}/kitinerary-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/kitinerary/c011fda7746c087a127999da1c4044854ee42238 || :
cp %{_builddir}/kitinerary-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kitinerary/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kitinerary/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kitinerary/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kitinerary/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kitinerary/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/ODbL-1.0.txt %{buildroot}/usr/share/package-licenses/kitinerary/fb63c741bc85425d4f0fa8b08a5ca2596d416ce9 || :
cp %{_builddir}/kitinerary-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kitinerary/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kitinerary-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kitinerary/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kitinerary-%{version}/src/cli/org.kde.kitinerary-extractor.desktop.license %{buildroot}/usr/share/package-licenses/kitinerary/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/kitinerary-%{version}/src/knowledgedb-generator/timezones.qgs.license %{buildroot}/usr/share/package-licenses/kitinerary/864bc0eb28c73bd997ac19ff91935ab771846615 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kitinerary
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf5/kitinerary-extractor
/usr/lib64/libexec/kf5/kitinerary-extractor

%files data
%defattr(-,root,root,-)
/usr/share/mime-packages/application-vnd-kde-itinerary.xml
/usr/share/qlogging-categories5/org_kde_kitinerary.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/KItinerary/AbstractExtractor
/usr/include/KPim5/KItinerary/Action
/usr/include/KPim5/KItinerary/AlphaId
/usr/include/KPim5/KItinerary/BERElement
/usr/include/KPim5/KItinerary/BarcodeDecoder
/usr/include/KPim5/KItinerary/BoatTrip
/usr/include/KPim5/KItinerary/Brand
/usr/include/KPim5/KItinerary/BusTrip
/usr/include/KPim5/KItinerary/CalendarHandler
/usr/include/KPim5/KItinerary/CountryDb
/usr/include/KPim5/KItinerary/CreativeWork
/usr/include/KPim5/KItinerary/Datatypes
/usr/include/KPim5/KItinerary/DocumentUtil
/usr/include/KPim5/KItinerary/ELBTicket
/usr/include/KPim5/KItinerary/Event
/usr/include/KPim5/KItinerary/ExtractorCapabilities
/usr/include/KPim5/KItinerary/ExtractorDocumentNode
/usr/include/KPim5/KItinerary/ExtractorDocumentNodeFactory
/usr/include/KPim5/KItinerary/ExtractorDocumentProcessor
/usr/include/KPim5/KItinerary/ExtractorEngine
/usr/include/KPim5/KItinerary/ExtractorFilter
/usr/include/KPim5/KItinerary/ExtractorPostprocessor
/usr/include/KPim5/KItinerary/ExtractorRepository
/usr/include/KPim5/KItinerary/ExtractorResult
/usr/include/KPim5/KItinerary/ExtractorValidator
/usr/include/KPim5/KItinerary/File
/usr/include/KPim5/KItinerary/Flight
/usr/include/KPim5/KItinerary/HtmlDocument
/usr/include/KPim5/KItinerary/IataBcbp
/usr/include/KPim5/KItinerary/IataBcbpSections
/usr/include/KPim5/KItinerary/JsonLdDocument
/usr/include/KPim5/KItinerary/KnowledgeDb
/usr/include/KPim5/KItinerary/LocationUtil
/usr/include/KPim5/KItinerary/MergeUtil
/usr/include/KPim5/KItinerary/Organization
/usr/include/KPim5/KItinerary/PdfDocument
/usr/include/KPim5/KItinerary/PdfImage
/usr/include/KPim5/KItinerary/PdfLink
/usr/include/KPim5/KItinerary/Person
/usr/include/KPim5/KItinerary/Place
/usr/include/KPim5/KItinerary/ProgramMembership
/usr/include/KPim5/KItinerary/Rct2Ticket
/usr/include/KPim5/KItinerary/RentalCar
/usr/include/KPim5/KItinerary/Reservation
/usr/include/KPim5/KItinerary/SSBTicketBase
/usr/include/KPim5/KItinerary/SSBv1Ticket
/usr/include/KPim5/KItinerary/SSBv2Ticket
/usr/include/KPim5/KItinerary/SSBv3Ticket
/usr/include/KPim5/KItinerary/ScriptExtractor
/usr/include/KPim5/KItinerary/SortUtil
/usr/include/KPim5/KItinerary/Taxi
/usr/include/KPim5/KItinerary/Ticket
/usr/include/KPim5/KItinerary/Token
/usr/include/KPim5/KItinerary/TrainTrip
/usr/include/KPim5/KItinerary/Uic9183Block
/usr/include/KPim5/KItinerary/Uic9183Header
/usr/include/KPim5/KItinerary/Uic9183Parser
/usr/include/KPim5/KItinerary/Uic9183TicketLayout
/usr/include/KPim5/KItinerary/Uic9183Utils
/usr/include/KPim5/KItinerary/VdvBasicTypes
/usr/include/KPim5/KItinerary/VdvTicket
/usr/include/KPim5/KItinerary/VdvTicketContent
/usr/include/KPim5/KItinerary/VdvTicketParser
/usr/include/KPim5/KItinerary/Vendor0080Block
/usr/include/KPim5/KItinerary/Vendor0080VUBlockData
/usr/include/KPim5/KItinerary/Vendor1154Block
/usr/include/KPim5/KItinerary/Visit
/usr/include/KPim5/kitinerary/abstractextractor.h
/usr/include/KPim5/kitinerary/action.h
/usr/include/KPim5/kitinerary/alphaid.h
/usr/include/KPim5/kitinerary/barcodedecoder.h
/usr/include/KPim5/kitinerary/berelement.h
/usr/include/KPim5/kitinerary/boattrip.h
/usr/include/KPim5/kitinerary/brand.h
/usr/include/KPim5/kitinerary/bustrip.h
/usr/include/KPim5/kitinerary/calendarhandler.h
/usr/include/KPim5/kitinerary/countrydb.h
/usr/include/KPim5/kitinerary/creativework.h
/usr/include/KPim5/kitinerary/datatypes.h
/usr/include/KPim5/kitinerary/documentutil.h
/usr/include/KPim5/kitinerary/elbticket.h
/usr/include/KPim5/kitinerary/event.h
/usr/include/KPim5/kitinerary/extractorcapabilities.h
/usr/include/KPim5/kitinerary/extractordocumentnode.h
/usr/include/KPim5/kitinerary/extractordocumentnodefactory.h
/usr/include/KPim5/kitinerary/extractordocumentprocessor.h
/usr/include/KPim5/kitinerary/extractorengine.h
/usr/include/KPim5/kitinerary/extractorfilter.h
/usr/include/KPim5/kitinerary/extractorpostprocessor.h
/usr/include/KPim5/kitinerary/extractorrepository.h
/usr/include/KPim5/kitinerary/extractorresult.h
/usr/include/KPim5/kitinerary/extractorvalidator.h
/usr/include/KPim5/kitinerary/file.h
/usr/include/KPim5/kitinerary/flight.h
/usr/include/KPim5/kitinerary/htmldocument.h
/usr/include/KPim5/kitinerary/iatabcbp.h
/usr/include/KPim5/kitinerary/iatabcbpsections.h
/usr/include/KPim5/kitinerary/internal/parameter_type.h
/usr/include/KPim5/kitinerary/jsonlddocument.h
/usr/include/KPim5/kitinerary/kitinerary_export.h
/usr/include/KPim5/kitinerary/knowledgedb.h
/usr/include/KPim5/kitinerary/locationutil.h
/usr/include/KPim5/kitinerary/mergeutil.h
/usr/include/KPim5/kitinerary/organization.h
/usr/include/KPim5/kitinerary/pdfdocument.h
/usr/include/KPim5/kitinerary/pdfimage.h
/usr/include/KPim5/kitinerary/pdflink.h
/usr/include/KPim5/kitinerary/person.h
/usr/include/KPim5/kitinerary/place.h
/usr/include/KPim5/kitinerary/programmembership.h
/usr/include/KPim5/kitinerary/rct2ticket.h
/usr/include/KPim5/kitinerary/rentalcar.h
/usr/include/KPim5/kitinerary/reservation.h
/usr/include/KPim5/kitinerary/scriptextractor.h
/usr/include/KPim5/kitinerary/sortutil.h
/usr/include/KPim5/kitinerary/ssbticketbase.h
/usr/include/KPim5/kitinerary/ssbv1ticket.h
/usr/include/KPim5/kitinerary/ssbv2ticket.h
/usr/include/KPim5/kitinerary/ssbv3ticket.h
/usr/include/KPim5/kitinerary/taxi.h
/usr/include/KPim5/kitinerary/ticket.h
/usr/include/KPim5/kitinerary/token.h
/usr/include/KPim5/kitinerary/traintrip.h
/usr/include/KPim5/kitinerary/uic9183block.h
/usr/include/KPim5/kitinerary/uic9183header.h
/usr/include/KPim5/kitinerary/uic9183parser.h
/usr/include/KPim5/kitinerary/uic9183ticketlayout.h
/usr/include/KPim5/kitinerary/uic9183utils.h
/usr/include/KPim5/kitinerary/vdvbasictypes.h
/usr/include/KPim5/kitinerary/vdvticket.h
/usr/include/KPim5/kitinerary/vdvticketcontent.h
/usr/include/KPim5/kitinerary/vdvticketparser.h
/usr/include/KPim5/kitinerary/vendor0080block.h
/usr/include/KPim5/kitinerary/vendor0080vublockdata.h
/usr/include/KPim5/kitinerary/vendor1154block.h
/usr/include/KPim5/kitinerary/visit.h
/usr/include/KPim5/kitinerary_version.h
/usr/lib64/cmake/KPim5Itinerary/KPim5ItineraryConfig.cmake
/usr/lib64/cmake/KPim5Itinerary/KPim5ItineraryConfigVersion.cmake
/usr/lib64/cmake/KPim5Itinerary/KPim5ItineraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5Itinerary/KPim5ItineraryTargets.cmake
/usr/lib64/cmake/KPimItinerary/KPim5ItineraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimItinerary/KPim5ItineraryTargets.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryConfig.cmake
/usr/lib64/cmake/KPimItinerary/KPimItineraryConfigVersion.cmake
/usr/lib64/libKPim5Itinerary.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5Itinerary.so.5.23.1
/usr/lib64/libKPim5Itinerary.so.5
/usr/lib64/libKPim5Itinerary.so.5.23.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kitinerary/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kitinerary/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kitinerary/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kitinerary/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kitinerary/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/kitinerary/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kitinerary/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/kitinerary/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/kitinerary/fb63c741bc85425d4f0fa8b08a5ca2596d416ce9
/usr/share/package-licenses/kitinerary/fca67987925d2ed70e898f6dd9c7fe4b458d416d

%files locales -f kitinerary.lang
%defattr(-,root,root,-)

