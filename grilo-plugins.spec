%define api	0.1

%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:		grilo-plugins
Version:	0.1.18
Release:	1
Summary:	Plugins for the Grilo framework
Group:		System/Libraries
License:	LGPLv2+
Url:		https://live.gnome.org/Grilo
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		grilo-plugins-0.1.18-tracker0.14-fix.patch

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmime-2.6)
BuildRequires:	pkgconfig(gupnp-1.0)
BuildRequires:	pkgconfig(gupnp-av-1.0)
#BuildRequires:	pkgconfig(libgdata)
BuildRequires:	libgdata-devel
BuildRequires:	pkgconfig(libquvi)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(tracker-sparql-0.12)
BuildRequires:	pkgconfig(grilo-0.1)

Requires:	grilo >= %{version}

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Filesystem
- Flickr
- Gravatar
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Podcasts
- Shoutcast
- Tracker
- UPnP
- Vimeo
- Youtube

%prep
%setup -q
%apply_patches

%build
#NOCONFIGURE=1 gnome-autogen.sh
%configure2_5x \
	--disable-static \
	--disable-fakemetadata \
	--disable-shoutcast \
	--enable-apple-trailers \
	--enable-bookmarks \
	--enable-fakemetadata \
	--enable-filesystem \
	--enable-flickr	\
	--enable-gravatar \
	--enable-jamendo \
	--enable-lastfm-albumart \
	--enable-localmetadata \
	--enable-metadata-store \
	--enable-podcasts \
	--enable-shoutcast \
	--enable-tracker \
	--enable-upnp \
	--enable-vimeo \
	--enable-youtube

%make

%install
%makeinstall_std

# Remove files that will not be packaged
find %{buildroot} -name "*.la" -delete

%files
%doc AUTHORS NEWS README
%{_libdir}/grilo-%{api}/grl-apple-trailers.xml
%{_libdir}/grilo-%{api}/libgrlappletrailers.so

%{_libdir}/grilo-%{api}/grl-bliptv.xml
%{_libdir}/grilo-%{api}/libgrlbliptv.so

%{_libdir}/grilo-%{api}/grl-bookmarks.xml
%{_libdir}/grilo-%{api}/libgrlbookmarks.so

%{_libdir}/grilo-%{api}/grl-fake-metadata.xml
%{_libdir}/grilo-%{api}/libgrlfakemetadata.so

%{_libdir}/grilo-%{api}/grl-filesystem.xml
%{_libdir}/grilo-%{api}/libgrlfilesystem.so

%{_libdir}/grilo-%{api}/grl-flickr.xml
%{_libdir}/grilo-%{api}/libgrlflickr.so

%{_libdir}/grilo-%{api}/grl-gravatar.xml
%{_libdir}/grilo-%{api}/libgrlgravatar.so

%{_libdir}/grilo-%{api}/grl-jamendo.xml
%{_libdir}/grilo-%{api}/libgrljamendo.so

%{_libdir}/grilo-%{api}/grl-lastfm-albumart.xml
%{_libdir}/grilo-%{api}/libgrllastfm-albumart.so

%{_libdir}/grilo-%{api}/grl-local-metadata.xml
%{_libdir}/grilo-%{api}/libgrllocalmetadata.so

%{_libdir}/grilo-%{api}/grl-metadata-store.xml
%{_libdir}/grilo-%{api}/libgrlmetadatastore.so

%{_libdir}/grilo-%{api}/grl-podcasts.xml
%{_libdir}/grilo-%{api}/libgrlpodcasts.so

%{_libdir}/grilo-%{api}/grl-shoutcast.xml
%{_libdir}/grilo-%{api}/libgrlshoutcast.so

%{_libdir}/grilo-%{api}/grl-tracker.xml
%{_libdir}/grilo-%{api}/libgrltracker.so

%{_libdir}/grilo-%{api}/grl-upnp.xml
%{_libdir}/grilo-%{api}/libgrlupnp.so

%{_libdir}/grilo-%{api}/grl-vimeo.xml
%{_libdir}/grilo-%{api}/libgrlvimeo.so

%{_libdir}/grilo-%{api}/grl-youtube.xml
%{_libdir}/grilo-%{api}/libgrlyoutube.so

