# Page generator

All pages in `admin/`, `provider/`, `user/` and `affiliate/` are generated from these modules
so the sidebar, top bar and components stay identical everywhere.

    python3 _build/gen_all.py     # from the repo root

- `gen_common.py`  shared sample data (providers, users, questions, posts, territories, FAQ), HTML helpers and the page shell
- `gen_p1.py … gen_p5.py`  admin console pages
- `gen_provider.py`  lawyer / professional portal (signed in as Amir A. Ladan)
- `gen_user.py`  consumer portal (signed in as Tom Becker)
- `gen_affiliate.py`  affiliate portal (signed in as Sunshine State Bail Bonds)

The runner also copies `admin/assets/{css,js,images}` into each portal folder, so edit the
design system in `admin/assets/css/admin.css` and re-run.
