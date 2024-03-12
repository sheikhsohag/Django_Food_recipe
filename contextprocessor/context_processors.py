def profile_picture(request):
    if request.user.is_authenticated:
        profile_image = request.user.userprofile.profile_image if hasattr(request.user, 'userprofile') else None
        return {'profile_image': profile_image}
    return {}