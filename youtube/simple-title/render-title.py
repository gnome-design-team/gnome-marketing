import bpy,os,re,sys

TITLE="Layers of GNOME 3"
 
def render():
 
  #bpy.context.scene.render.resolution_percentage =
  #bpy.context.scene.render.use_compositing = 0
  #bpy.context.scene.render.use_sequencer = 1
  renderpath = '//out/%s - ' % TITLE[:5]
  bpy.context.scene.render.filepath = renderpath
  
  if (not os.path.isdir(renderpath)):
    #print('yay')
    bpy.ops.render.render(animation=True)
  else:
    print('already rendered',bpy.context.scene.render.frame_path())

  
#translates strings and calls render
def main():

    #
    #bpy.data.objects[textobj.get('id')].data.body = textobj.text
    #bpy.data.objects['usermenuuser'].data.body = bpy.data.objects['user'].data.body #due to different alignment
    bpy.data.objects['Text'].data.body = TITLE
    render()
    
if __name__ == '__main__':
    main()
