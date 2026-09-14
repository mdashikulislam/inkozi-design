import sys, os, shutil, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_common
import gen_p1, gen_p2, gen_p3, gen_p4, gen_p5, gen_provider, gen_user, gen_affiliate
for m in (gen_p1, gen_p2, gen_p3, gen_p4, gen_p5, gen_provider, gen_user, gen_affiliate):
    m.build()
# keep portal assets in sync with admin
root = gen_common.ROOT
for d in ('provider', 'user', 'affiliate'):
    for sub in ('css', 'js', 'images'):
        dst = f'{root}{d}/assets/{sub}'
        shutil.rmtree(dst, ignore_errors=True)
        shutil.copytree(f'{root}admin/assets/{sub}', dst)
print('assets synced;', sum(len(glob.glob(f'{root}{d}/*.html')) for d in ('admin','provider','user','affiliate')), 'pages total')
