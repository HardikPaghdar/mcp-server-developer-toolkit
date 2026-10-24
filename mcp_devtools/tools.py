from pathlib import Path
import os
EXT={'.py','.js','.ts','.md','.txt','.json','.yaml','.toml'}; SKIP={'.git','.venv','venv','node_modules','__pycache__'}
class Workspace:
    def __init__(self,root=None):
        self.root=Path(root or os.environ.get('PROJECT_ROOT','.')).expanduser().resolve()
        if not self.root.is_dir(): raise ValueError('PROJECT_ROOT must be an existing directory')
    def files(self):
        return sorted(p for p in self.root.rglob('*') if p.is_file() and not p.is_symlink() and p.suffix.lower() in EXT and not any(x in SKIP for x in p.relative_to(self.root).parts) and p.stat().st_size<500000)
    def resolve(self,rel):
        if not rel or Path(rel).is_absolute(): raise ValueError('Relative path required')
        p=(self.root/rel).resolve()
        if p!=self.root and self.root not in p.parents: raise ValueError('Path escapes workspace')
        if p.is_symlink(): raise ValueError('Symlink access blocked')
        return p
    def listing(self,limit=100):
        if not 1<=limit<=500: raise ValueError('Limit must be 1..500')
        fs=self.files(); return {'count':len(fs),'files':[p.relative_to(self.root).as_posix() for p in fs[:limit]]}
    def read(self,rel):
        p=self.resolve(rel)
        if p not in self.files(): raise ValueError('File is not eligible')
        return {'path':p.relative_to(self.root).as_posix(),'content':p.read_text(encoding='utf-8',errors='replace')}
    def search(self,q,limit=20):
        if len(q.strip())<2 or not 1<=limit<=100: raise ValueError('Invalid query or limit')
        hits=[]
        for p in self.files():
            for no,line in enumerate(p.read_text(encoding='utf-8',errors='replace').splitlines(),1):
                if q.casefold() in line.casefold(): hits.append({'path':p.relative_to(self.root).as_posix(),'line':no,'text':line.strip()[:500]})
                if len(hits)>=limit: return {'query':q,'matches':hits}
        return {'query':q,'matches':hits}
