odoo.define("DhtmlxGanttView", function (require) {
  "use strict";

  const OWLController = require("DhtmlxGanttController");
  const OWLModel = require("DhtmlxGanttModel");
  const OWLRenderer = require("DhtmlxGanttRenderer");
  const AbstractView = require("web.AbstractView");
  const RendererWrapper = require("web.RendererWrapper");
  const view_registry = require("web.view_registry");


  const DhtmlxGanttView = AbstractView.extend({
    accesskey: "m",
    display_name: "Vue Dhtmlx Gantt",
    icon: "fa-indent",
    config: _.extend({}, AbstractView.prototype.config, {
      Controller: OWLController,
      Model: OWLModel,
      Renderer: OWLRenderer,
    }),
    viewType: "dhtmlx_gantt_task",

    /**
     * @override
     */
    init: function () {
      this._super.apply(this, arguments);
    },

    getRenderer(parent, state) {
      state = Object.assign(state || {}, this.rendererParams);
      return new RendererWrapper(parent, this.config.Renderer, state);
    },
  });

  view_registry.add("dhtmlx_gantt_task", DhtmlxGanttView);
  return DhtmlxGanttView;
});
