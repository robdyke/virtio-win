Name:		virtio-win
Version:	0.1
Release:	81.1%{?dist}
Summary:	Windows guest drivers
Group:		FIXME
License:	Unknown
URL:		http://www.linux-kvm.org/page/WindowsGuestDrivers
#Source0:	http://alt.fedoraproject.org/pub/alt/virtio-win/latest/images/bin/%{name}-0.1-81.iso
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#BuildRequires:	xorriso
BuildArch:	noarch

%description
Windows guest drivers

%prep
mkdir -p %{_builddir}/%{name}-%{version}
wget  http://alt.fedoraproject.org/pub/alt/virtio-win/latest/images/bin/%{name}-0.1-81.iso -O /tmp/%{name}.iso
mount -o loop /tmp/%{name}.iso /mnt
cp -dpR /mnt/* %{_builddir}/%{name}-%{version}
umount /mnt
#xorriso -osirrox on -indev %{SOURCE0} -extract / %{_builddir}/%{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/amd64
mkdir -p %{buildroot}/usr/share/virtio-win/drivers/i386
cp -r %{_builddir}/%{name}-%{version}/xp/amd64   %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2003
cp -r %{_builddir}/%{name}-%{version}/win7/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win2008
cp -r %{_builddir}/%{name}-%{version}/win7/amd64 %{buildroot}/usr/share/virtio-win/drivers/amd64/Win7
cp -r %{_builddir}/%{name}-%{version}/xp/amd64   %{buildroot}/usr/share/virtio-win/drivers/amd64/WinXP
cp -r %{_builddir}/%{name}-%{version}/xp/x86     %{buildroot}/usr/share/virtio-win/drivers/i386/Win2003
cp -r %{_builddir}/%{name}-%{version}/win7/x86   %{buildroot}/usr/share/virtio-win/drivers/i386/Win2008
cp -r %{_builddir}/%{name}-%{version}/win7/x86   %{buildroot}/usr/share/virtio-win/drivers/i386/Win7
cp -r %{_builddir}/%{name}-%{version}/xp/x86     %{buildroot}/usr/share/virtio-win/drivers/i386/WinXP

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
/usr/share/virtio-win

%changelog
* Sun 09 Aug 2014 Neova Health <office@neovahealth.co.uk> - 0.1-81.1
- Bump to 1.81
* Fri May 25 2012 Harvard University FAS Research Computing <rchelp@fas.harvard.edu> - 0.1-22.1
- Initial package
