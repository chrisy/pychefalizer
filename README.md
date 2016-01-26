# Python Chefalizer

More README coming soon!

Pipe English into stdin and get Chefalized text out of it!

# Example usage

If you have some text, such as this excerpt from
[Wikipedia](https://en.wikipedia.org/wiki/Swedish_Chef) in a file named `sample.txt`:

> A parody of television chefs, the Swedish Chef wears a toque blanche and has
> bushy eyebrows that completely obscure his eyes. He was one of the few
> Muppets to employ an actual puppeteer's hands, originally Oz's, in the
> designs – that is, they were visible to the audience through his sleeves
> and facilitated handling food and utensils.
>
> Nearly all Swedish Chef sketches on The Muppet Show begin featuring him within
> a kitchen environment, waving some utensils while singing his signature
> yodel-esque song in his typical mock Swedish – a semi-comprehensible gibberish
> mimicking Swedish phonology and prosody. The song's lyrics vary slightly from
> one episode to the next, but always end with "Bork, bork, bork!" as the Chef
> throws the utensils (or whatever else may be in his hands) aside with a
>  clatter that seems to startle him.
>
> After this introduction, the Chef begins to prepare a recipe while giving a
> gibberish explanation of what he is doing. His commentary is spiced with the
> occasional English word to clue in the viewer to what he is attempting; for
> example, "Aweenda shmure da froog's legs" or "Yur puurt thuur chiir-ken airn
> der bewl". These hints are necessary as he frequently uses unorthodox culinary
> equipment (firearms, sports equipment, hand tools, etc.) to prepare his dishes.
> In the pilot episode of The Muppet Show, the Chef's commentary was
>  supplemented by Chinese subtitles,[citation needed] but this was abandoned
> for all other episodes of the series. The sketch typically degenerates into a
> slapstick finale where the equipment or ingredients (usually a live
> chicken/goat/cow etc.) get the better of him.

Then executing `./chefalizer < sample.txt' would produce the following output:

> A perudy ooff telefeesiun cheffs, zee Svedish Cheff veers a tuqooe-a
> blunche-a und hes booshy iyebroos thet cumpletely oobscoore-a his iyes.
> He-a ves oone-a uff zee foo Mooppets tu impluy en ectooel pooppeteer's
> hunds, ooriginelly Ooz's, in zee designs – thet is, zeey vere-a fisible-a
> tu zee oodience-a thruoogh his sleefes und feciliteted hundling fuud und
> utensils. Bork bork bork.
>
> Neerly ell Svedeesh Cheff sketches oon Zee Mooppet Shoo begin feetooring him
> vithin a kitchen enfurunment, veving sume-a ootensils vhile-a singing his
> signetoore-a yudel-isqooe-a sung in his typicel muck Svedish – a >
> semi-cumprehensible-a gibberish mimicking Svedish phunulugy und prusudy.
> Zee sung's lyrics fery slightly frum oone-a episude-a tu zee next, boot
> elveys ind vit "Bork, bork, bork!" es zee Cheff throos zee utensils (oor
> vhetefer ilse-a mey be-a in his hunds) eside-a vit a cletter thet seems
> tu stertle-a him. Bork bork bork.

> Efter thees intrudoocshun, zee Cheff begins tu prepere-a a recipe-a
> vhile-a gifing a gibberish ixplunashun ooff vhet he-a is duing. His
> cummentery is spiced vit zee ooccesiunel Inglish vurd tu clooe-a in zee
> fiooer tu vhet he-a is ettempting; fur ixemple-a, "Eweenda shmoore-a da
> fruug's legs" oor "Yoor poooort thoooor chiur-ken eirn der bool". Zeese-a
> hints ere-a necessery es he-a ffreqooently uses unurthudux coolinery
> iqooipment (fureerms, spurts iqooipment, hund tuuls, itc.) tu prepere-a
> his dishes. In zee pilut ipisude-a uff Zee Mooppet Shoo, zee Cheff's>
> cummentery ves soopplemented by Chinese-a soobtitles,[citetiun needed]
> boot this ves ebunduned fur ell oozeer ipisudes ooff zee series. Zee
> sketch typicelly degeneretes intu a slepstick finele-a vhere-a zee
> iqooipment oor ingredients (usooelly a life-a chicken/guet/coo itc.)
> get zee better ooff him. Bork bork bork.


